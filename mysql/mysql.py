# # 导入MySQL驱动:
# import pymysql
# # 注意把password设为你的root口令:
# conn=pymysql.connect(user='root',password='', host='localhost',database='test')

# cursor=conn.cursor()
# #cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')

# cursor.execute('insert into users(id,name) values (%s,%s)',['no2','jake'])
# conn.commit()
# print('成功插入', cursor.rowcount, '条数据')  
# cursor.close()

# cursor=conn.cursor()
# cursor.execute('select * from users where id=%s',('no1',))
# vs=cursor.fetchall()
# print(vs)
# cursor.close()

# conn.close()


from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class User(Base):

	__tablename__='users'


	id=Column(String(20),primary_key=True)
	name=Column(String(20))

	books=relationship('Book')

class Book(Base):

	__tablename__='books'

	id=Column(String(20),primary_key=True)
	name=Column(String(20))
	
	# “多”的一方的book表是通过外键关联到user表的:
	users_id=Column(String(20),ForeignKey('users.id'))

engine=create_engine('mysql+pymysql://root:@localhost:3306/test')

DBSession=sessionmaker(bind=engine)

session=DBSession()

#插入数据
# new_user=User(id='no3',name='Bob')
# session.add(new_user)
# session.commit()
# session.close()

#读取数据
user=session.query(User).filter(User.id=='no1').one()
print(user.name)
# print(user.books[0].users_id)
for i in user.books:
	print(i.id,i.name,i.users_id)
session.close()