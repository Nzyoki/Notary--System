from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Document, User
from app import db

bp = Blueprint('notary', __name__)

@bp.route('/notary/dashboard')
@login_required
def dashboard():
    if not current_user.is_notary:
        flash('Access denied.', 'danger')
        return redirect(url_for('document.dashboard'))
    documents = Document.query.filter((Document.notary_id == current_user.id) | (Document.notary_id == None)).all()
    return render_template('notary_dashboard.html', documents=documents)

@bp.route('/notary/assign/<int:document_id>')
@login_required
def assign(document_id):
    if not current_user.is_notary:
        flash('Access denied.', 'danger')
        return redirect(url_for('document.dashboard'))
    document = Document.query.get_or_404(document_id)
    if document.notary_id is None:
        document.notary_id = current_user.id
        db.session.commit()
        flash('Document assigned to you.', 'success')
    else:
        flash('Document already assigned.', 'danger')
    return redirect(url_for('notary.dashboard'))

@bp.route('/notary/approve/<int:document_id>')
@login_required
def approve(document_id):
    if not current_user.is_notary:
        flash('Access denied.', 'danger')
        return redirect(url_for('document.dashboard'))
    document = Document.query.get_or_404(document_id)
    if document.notary_id == current_user.id:
        document.status = 'approved'
        db.session.commit()
        flash('Document approved.', 'success')
    else:
        flash('You are not assigned to this document.', 'danger')
    return redirect(url_for('notary.dashboard'))