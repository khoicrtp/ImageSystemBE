import mysql.connector

#mysql://ba210f51bd8223:9bc50fbc@us-cdbr-east-05.cleardb.net/heroku_d08923bbc460fa4?reconnect=true
mydb = mysql.connector.connect(
  host="us-cdbr-east-05.cleardb.net",
  user="ba210f51bd8223",
  password="9bc50fbc",
  database="heroku_d08923bbc460fa4" # DEFAULT SCHEMA
)
mycursor = mydb.cursor()

def insertUser(username, password, publickey): 
  sql = "INSERT INTO ACCOUNT (USERNAME, PASSWORD, PUBLICKEY) VALUES (%s, %s, %s);"
  val = (username, password, publickey)
  mycursor.execute(sql, val)
  mydb.commit()

def selectUser(username):
  sql = "SELECT * FROM ACCOUNT WHERE USERNAME = %s;"
  val = (username,)
  mycursor.execute(sql, val)
  res = mycursor.fetchall()
  return res

def selectAllUser():
  sql = "SELECT * FROM ACCOUNT;"
  mycursor.execute(sql)
  res = mycursor.fetchall()
  return res

def insertImage(username, image_url):
  sql = "INSERT INTO IMAGE (USERNAME, IMAGE_URL) VALUES (%s, %s);"
  val = (username, image_url)
  mycursor.execute(sql, val)
  mydb.commit()

def selectAllImage(username):
  sql = "SELECT IMAGE_URL FROM IMAGE WHERE USERNAME = %s;"
  val = (username,)
  mycursor.execute(sql, val)
  res = mycursor.fetchall()
  return res

# insertImage('suir', '/abc')

# userID={"username": "UOa2", "password": "abc", "key":"1234"}

# path = userID["username"]+"/"

# insertUser("suir", "a", "638")

#print(selectAll())
# print("running")