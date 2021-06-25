from flask import Blueprint,request
from app.models.model import Book

bp=Blueprint('bp',__name__)

@bp.route('/')
def gett():
    books=Book.objects.all()
    for i in books:
        print(i.to_json())
    return "check"

@bp.route('/',methods=['POST'])
def add():
    book=Book(name="FF",author="S")
    book.save()
    return "Added!"

@bp.route('/',methods=['PUT'])
def update():
    book=Book.objects(name="nn").update(
        author="Soni"
    )
    return "Updated!"

@bp.route('/',methods=['DELETE'])
def delete():
    Book.objects(name="FF").delete()
    return "Delete!"