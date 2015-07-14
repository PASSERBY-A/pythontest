 

# -*- coding: utf-8 -*-




import winsound
import psycopg2
import time


# select * from tf_avmon_notify
# update  tf_avmon_notify   set  send_flag=0  
# select * from tf_avmon_alarm_data order by last_occur_time desc
# select * from tf_avmon_alarm_history order by last_occur_time desc 



mp3 = 'alert_msg.wav'
phoneNo='13900000000'
host='localhost'
port=5432
password='password'
user='postgres'
database='avmon'

#insert into tf_avmon_notify  values('13900000000','一条告警',current_timestamp,current_timestamp,current_timestamp,'id',0,0,'告警','eee',1);

def playNotifyMp3():
    
    while 1==1:
        
        winsound.PlaySound(mp3, winsound.SND_NODEFAULT)

def getConnection():

    return psycopg2.connect(database=database, user=user, password=password, host=host, port=port);

def release(conn,cur):
    
     cur.close()
     
     conn.close()
    
    
    
    

def updateNotifyRow(id):
    
    try:
         conn = getConnection();
    
         cur = conn.cursor();
         
         cur.execute("update  tf_avmon_notify set  send_flag=1 where id='"+id+"' ");
         
         playNotifyMp3();
    
    finally:
        
        conn.commit()
         
        release(conn,cur)   
       

if __name__ == '__main__':
    
    while(True):
        try:
            
            time.sleep(3);
        
            conn = getConnection()
            
            cur = conn.cursor();
            
            cur.execute("SELECT * FROM tf_avmon_notify t where t.send_flag=0 and t.phone_no='"+phoneNo+"';")
        
            rows = cur.fetchall()  
                  # all rows in table
            for i in rows:
                updateNotifyRow(i[9])
    
        finally:
        
            conn.commit()
            release(conn,cur)
