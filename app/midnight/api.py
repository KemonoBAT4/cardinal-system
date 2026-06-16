
# local imports
from ._common import *
from .models import *

api = Blueprint(f'{project_name}_api', __name__)

@api.route("/user/info", methods=['GET'])
@jwt_required()
def user_info():
    current_user_uname  = get_jwt_identity()
    user: "User | None" = User.query.filter(User.uname == current_user_uname).first()

    if user is None:
        return jsonify({"status": False, "message": "User not found"}), 401
    # #endif

    return jsonify({"data": user.to_dict()}), 200
# #enddef user_info

@api.route("/tasks/list", methods=['GET', 'POST'])
@jwt_required()
def tasks_list():
    current_user_uname  = get_jwt_identity()
    user: "User | None" = User.query.filter(User.uname == current_user_uname).first()

    if user is None:
        return jsonify({"status": False, "message": "User not found"}), 401
    # #endif

    tasks: list[Task] = Task.query.filter(Task.user_id == user.id).all()
    return jsonify({"data": [task.to_dict() for task in tasks]})
# #enddef table_tasks_list

@api.route("/tasks/new", methods=['POST'])
@jwt_required()
def tasks_new():
    current_user_uname  = get_jwt_identity()
    user: "User | None" = User.query.filter(User.uname == current_user_uname).first()

    data = request.get_json()

    if user is None:
        return jsonify({"status": False, "message": "User not found"}), 401
    # #endif

    task: Task = Task.new(
        title       = data.get("title", f"Undefined Task - {uuid.uuid4().hex[:4]}"),
        user_id     = user.id,
        description = data.get("description", ""  ),
        from_date   = datetime.datetime.fromisoformat(data.get("from_date"  , None)),
        to_date     = datetime.datetime.fromisoformat(data.get("to_date"    , None))
    )
    task.save()

    return jsonify({"data": task.to_dict()}), 200
# #enddef tasks_new

@api.route("/task/edit/<int:task_id>", methods=['POST'])
@jwt_required()
def task_edit(task_id: int):
    current_user_uname  = get_jwt_identity()
    user: "User | None" = User.query.filter(User.uname == current_user_uname).first()

    data = request.get_json()

    if user is None:
        return jsonify({"status": False, "message": "User not found"}), 200
    # #endif

    task: "Task | None" = Task.query.filter(Task.id == task_id).first()

    if task is None:
        return jsonify({"status": False, "message": "Task not found"}), 200
    # #endif

    title       = data.get("title"      , None)
    description = data.get("description", None)
    from_date   = data.get("from_date"  , None)
    to_date     = data.get("to_date"    , None)

    task.title       = title       if title       is not None else task.title
    task.description = description if description is not None else task.description
    task.from_date   = from_date   if from_date   is not None else task.from_date
    task.to_date     = to_date     if to_date     is not None else task.to_date

    task.save()

    return jsonify({"data": task.to_dict()}), 200
# #enddef task_edit

@api.route("/notes/list", methods=['GET', "POST"])
@jwt_required()
def notes_list():
    current_user_uname  = get_jwt_identity()
    user: "User | None" = User.query.filter(User.uname == current_user_uname).first()

    if user is None:
        return jsonify({"status": False, "message": "User not found"}), 401
    # #endif

    notes: list[Note] = Note.query.filter(Note.user_id == user.id).all()
    return jsonify({"data": [note.to_dict() for note in notes]})
# #enddef notes_list

@api.route("/notes/new", methods=['POST'])
@jwt_required()
def notes_new():
    current_user_uname  = get_jwt_identity()
    user: "User | None" = User.query.filter(User.uname == current_user_uname).first()

    data = request.get_json()

    if user is None:
        return jsonify({"status": False, "message": "User not found"}), 401
    # #endif

    note: Note = Note.new(
        title = data.get("title", f"Undefined Note - {uuid.uuid4().hex[:4]}"),
        user_id = user.id,
        text = data.get("text", "")
    )
    note.save()

    return jsonify({"data": note.to_dict()}), 200
# #enddef tasks_new
@api.route("/note/edit/<int:task_id>", methods=['POST'])
@jwt_required()
def note_edit(note_id: int):
    current_user_uname  = get_jwt_identity()
    user: "User | None" = User.query.filter(User.uname == current_user_uname).first()

    data = request.get_json()

    if user is None:
        return jsonify({"status": False, "message": "User not found"}), 200
    # #endif

    note: "Note | None" = Note.query.filter(Note.id == note_id).first()

    if note is None:
        return jsonify({"status": False, "message": "Note not found"}), 200
    # #endif

    title = data.get("title", None)
    text  = data.get("text" , None)

    note.title = title if title is not None else note.title
    note.text  = text  if text  is not None else note.text

    note.save()

    return jsonify({"data": note.to_dict()}), 200
# #enddef task_edit



@api.route("/auth/login", methods=['POST'])
def login():

    data = request.get_json()
    user_or_tuple: "User | tuple" = User.login(
        username = data.get("username", ""),
        password = data.get("password", "")
    )

    if (isinstance(user_or_tuple, tuple)):
        return jsonify({"status": False, "message": user_or_tuple[1]}), 401
    # #endif

    token: str = create_access_token(identity=user_or_tuple.uname)
    return jsonify({"status": True, "token": token}), 200
# #enddef login

@api.route("/auth/register", methods=['POST'])
def register():

    data = request.get_json()
    user_or_tuple: "User | tuple" = User.register(**data)

    if isinstance(user_or_tuple, tuple):
        return jsonify({"status": user_or_tuple[0], "message": user_or_tuple[1]}), 401
    # #endif

    token: str = create_access_token(identity=user_or_tuple.uname)
    return jsonify({"status": True, "token": token}), 200
# #enddef register
