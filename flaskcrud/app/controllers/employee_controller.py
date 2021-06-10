from flask import Blueprint,request,jsonify
from app.models.models import Employee
from app.database.connect import sess

bp = Blueprint('bp',__name__)


@bp.route('/employee/add',methods=['POST'])
def create():
    try:
        data=request.get_json()

        if data.get('title')==None:
            raise Exception('ERROR title is empty')
        if data.get('experience')==None:
            raise Exception('ERROR experience is empty')

        emp=Employee(**data)
        sess.add(emp)
        sess.commit()
        return jsonify({"data":data})
    except Exception as e:
        return {"error":str(e)}


@bp.route('/employee/<int:id>/delete',methods=['DELETE'])
def delete_Employee(id):
    try:
        emp=sess.query(Employee).filter_by(id=id).first()
        if emp==None:
            return "User Doesn't Exist!"
        sess.delete(emp)
        sess.commit()
        return "Deleted!!!"
    except Exception as e:
        return {"error":str(e)}


@bp.route('/employee/<int:id>/update',methods=['PUT'])
def updatedata(id):
    try:
        data=request.get_json()
        sess.query(Employee).filter_by(id=id).update(data)

        sess.commit()
        return "Updatedddd!"
    except Exception as e:
        return {"error":str(e)}

@bp.route('/employee/<int:id>/fetch',methods=['GET'])
def fet(id):
    try:
        emp=sess.query(Employee).filter_by(id=id).first()
        if emp==None:
            return "User Doesn't Exist!"
        return {"id":id,"data":{"title":emp.title,"dept":emp.department,"country":emp.country,"state":emp.state,"city":emp.city,"remote":emp.remote,"description":emp.description,"requirements":emp.requirements,"benifit":emp.benifits,"comind":emp.company_industry,"job_fun":emp.job_function,"employment_type":emp.employment_type,"experience":emp.experience,"education":emp.education,"keywords":emp.keywords,"salaryFrom":emp.salary_from,"salaryTo":emp.salary_to,"currency":emp.currency}}
    except Exception as e:
        return {"Error":str(e)}

@bp.route('/employee/fetchall',methods=['GET'])
def fetch():
    try:
        emp=sess.query(Employee).all()
        if len(emp)==0:
            return "Empty DataBase"
        return {"data":[i.title for i in emp]}
    except Exception as e:
        return {"Error":str(e)}
