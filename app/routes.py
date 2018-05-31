from app import app

@app.route('/')
@app.route('/index')


def index():
    return "hello world";

@app.route('/login')

def login():
    pass


@app.route('/signup')

def signup():
    pass

@app.route('/logout')

def logout():
    pass

@app.route('/getrequests')

def getrequests():
    pass
@app.route('/getrequest')

def getrequest():
    pass
@app.route('/editrequest')

def editrequest():
    pass

@app.route('/deleterequest')

def deleterequest():
    pass

@app.route('/modifyrequest')

def modifyrequest():
    pass
@app.route('/createrequest')

def createrequest():
    pass

