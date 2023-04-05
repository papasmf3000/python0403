# db1.py 
import sqlite3

#메모리에 임시로 작업
#con = sqlite3.connect(":memory:")
#실제 파일에 저장하기
con = sqlite3.connect(":memory:")
cur = con.cursor() 
#테이블 생성(데이터구조)
cur.execute("create table if not exists PhoneBook " 
    + "(id integer primary key autoincrement, "
    + " name text, phoneNum text);") 
#1건 입력 
cur.execute("insert into PhoneBook (name, phoneNum) values "
    + " ('홍길동','010-111');")
#외부에서 입력파라메터로 받기
name = "이순신"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values "
    + " (?, ?);", (name, phoneNumber) )
#다중의 행을 입력(2차원 배열) 
datalist = (("전우치","010-333"), ("박문수","010-1234"))
cur.executemany("insert into PhoneBook (name, phoneNum) values "
    + " (?, ?);", datalist )

#검색
cur.execute("select * from PhoneBook;")
print("---fetchone()---")
print( cur.fetchone() )
print("---fetchmany(2)---")
print( cur.fetchmany(2) )
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )


#정상적으로 완료
con.commit()


