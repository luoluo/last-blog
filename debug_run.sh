export FLASK_APP=main.py
export FLASK_DEBUG=1
# note: using the 0.0.0.0 address make the server externally visible.
flask run --host=0.0.0.0 --port=5002
