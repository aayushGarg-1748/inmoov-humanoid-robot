#firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('cyborg-c343f-firebase-adminsdk-23k57-8ea068b4b7.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
def adminAuth():
    usrnm = "ayush garg"
    
    doc_ref = db.collection('credentials').document(usrnm)
    doc = doc_ref.get()
    
    passwor = "175 cb 85"
    op = "dumb fuck fuck no yes"
    
    if 'yes' in op:
        if doc.exists:
            document = format(doc.to_dict())
            obj = eval(document)
            admin = obj.get("admin")
            passwr = obj.get("password")
            print(passwr)
            if(passwr == passwor):
                if (admin == True):
                    print("admin-auth successful")
                    return True
                else: return False
            else:
                return False

        else:
            print('No such document!')
            return False
    if 'no' in op:
        return False;

if (adminAuth()== True):
    print("admin login success")
