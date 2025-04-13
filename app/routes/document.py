from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_required, current_user
from app.models import Document
from app import db
import os
from werkzeug.utils import secure_filename

bp = Blueprint('document', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@bp.route('/dashboard')
@login_required
def dashboard():
    documents = Document.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', documents=documents)

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part.', 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected.', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            document = Document(filename=filename, filepath=filepath, user_id=current_user.id)
            db.session.add(document)
            db.session.commit()
            flash('Document uploaded successfully!', 'success')
            return redirect(url_for('document.dashboard'))
        flash('Invalid file type.', 'danger')
    return render_template('upload.html')

@bp.route('/edit/<int:document_id>', methods=['GET', 'POST'])
@login_required
def edit(document_id):
    document = Document.query.get_or_404(document_id)
    if document.user_id != current_user.id:
        flash('You do not have permission to edit this document.', 'danger')
        return redirect(url_for('document.dashboard'))
    
    if request.method == 'POST':
        new_filename = request.form.get('filename')
        file = request.files.get('file')
        
        if new_filename:
            document.filename = secure_filename(new_filename)
        
        if file and allowed_file(file.filename):
            # Delete old file
            if os.path.exists(document.filepath):
                os.remove(document.filepath)
            # Save new file
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            document.filename = filename
            document.filepath = filepath
        
        db.session.commit()
        flash('Document updated successfully!', 'success')
        return redirect(url_for('document.dashboard'))
    
    return render_template('edit_document.html', document=document)

@bp.route('/delete/<int:document_id>', methods=['POST'])
@login_required
def delete(document_id):
    document = Document.query.get_or_404(document_id)
    if document.user_id != current_user.id:
        flash('You do not have permission to delete this document.', 'danger')
        return redirect(url_for('document.dashboard'))
    
    # Delete file from filesystem
    if os.path.exists(document.filepath):
        os.remove(document.filepath)
    
    # Delete from database
    db.session.delete(document)
    db.session.commit()
    flash('Document deleted successfully!', 'success')
    return redirect(url_for('document.dashboard'))