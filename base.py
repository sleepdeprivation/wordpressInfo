import mysql.connector
import database

versionLookup = {'2540' : '1.2.2','2541' : '1.5','2541' : '1.5.1','2541' : '1.5.1.1','2541' : '1.5.1.2','2541' : '1.5.1.3','2541' : '1.5.2','3441' : '2.0','3441' : '2.0.1','3441' : '2.0.2','3441' : '2.0.3','3441' : '2.0.4','3441' : '2.0.5','3441' : '2.0.6','3441' : '2.0.7','3441' : '2.0.8','3441' : '2.0.9','3441' : '2.0.10','3441' : '2.0.11','4772' : '2.1','4773' : '2.1.1','4773' : '2.1.2','4773' : '2.1.3','5183' : '2.2','5183' : '2.2.1','5183' : '2.2.2','5183' : '2.2.3','6124' : '2.3','6124' : '2.3.1','6124' : '2.3.2','6124' : '2.3.3','7558' : '2.5','7796' : '2.5.1','8201' : '2.6','8204' : '2.6.1','8204' : '2.6.2','8204' : '2.6.3','8204' : '2.6.5','9872' : '2.7','9872' : '2.7.1','11548' : '2.8','11548' : '2.8.1','11548' : '2.8.2','11548' : '2.8.3','11548' : '2.8.4','11548' : '2.8.5','11548' : '2.8.6','12329' : '2.9','12329' : '2.9.1','12329' : '2.9.2','15260' : '3.0','15477' : '3.0.1','15477' : '3.0.2','15477' : '3.0.3','15477' : '3.0.4','15477' : '3.0.5','15477' : '3.0.6','17056' : '3.1','17516' : '3.1.1','17516' : '3.1.2','17516' : '3.1.3','17516' : '3.1.4','18226' : '3.2','18226' : '3.2.1','19470' : '3.3','19470' : '3.3.1','19470' : '3.3.2','19470' : '3.3.3','20596' : '3.4','21115' : '3.4.1','21707' : '3.4.2','22441' : '3.5','22441' : '3.5.1','22442' : '3.5.2','24448' : '3.6','24448' : '3.6.1','25824' : '3.7','25824' : '3.7.1','26148' : '3.7.2','26149' : '3.7.3','26149' : '3.7.4','26149' : '3.7.5','26149' : '3.7.6','26149' : '3.7.7','26151' : '3.7.8','26151' : '3.7.9','26151' : '3.7.10','26151' : '3.7.11','26151' : '3.7.12','26151' : '3.7.13','26691' : '3.8','26691' : '3.8.1','26691' : '3.8.2','26692' : '3.8.3','26692' : '3.8.4','26692' : '3.8.5','26692' : '3.8.6','26692' : '3.8.7','26694' : '3.8.8','26694' : '3.8.9','26694' : '3.8.10','26694' : '3.8.11','26694' : '3.8.12','26694' : '3.8.13','27916' : '3.9','27916' : '3.9.1','27916' : '3.9.2','27916' : '3.9.3','27916' : '3.9.4','27916' : '3.9.5','27918' : '3.9.6','27918' : '3.9.7','27918' : '3.9.8','27918' : '3.9.9','27918' : '3.9.10','29632' : '3.9.11','29630' : '4.0','29630' : '4.0.1','29630' : '4.0.2','29630' : '4.0.3','29631' : '4.0.4','29632' : '4.0.5','29632' : '4.0.6','29632' : '4.0.7','29632' : '4.0.8','29632' : '4.0.9','29632' : '4.0.10','30133' : '4.1','30133' : '4.1.1','30133' : '4.1.2','30133' : '4.1.3','30134' : '4.1.4','30135' : '4.1.5','30135' : '4.1.6','30135' : '4.1.7','30135' : '4.1.8','30135' : '4.1.9','30135' : '4.1.10','31532' : '4.2','31533' : '4.2.1','31535' : '4.2.2','31536' : '4.2.3','31536' : '4.2.4','31536' : '4.2.5','31536' : '4.2.6','31536' : '4.2.7','33055' : '4.3','33056' : '4.3.1','33056' : '4.3.2','33056' : '4.3.3','35700' : '4.4','35700' : '4.4.1','35700' : '4.4.2','36686' : '4.5','36686' : '4.5.1'}

def getConnection(dbname):
    return database.getConnection(dbname)


def getDBusers():
    cnx = getConnection("information_schema")
    cursor = cnx.cursor()
    query = ("select table_schema, table_name from tables where table_name like \"%wp_users%\";")
    cursor.execute(query)
    retval = {}
    #get database version numbers
    for item in cursor:
        #print(item[0])
        newCon = getConnection(item[0])
        c1 = newCon.cursor()
        query2 = ("select user_login from "+item[1])
        c1.execute(query2)
        res = c1.fetchall()
        #print res
        retval[item[0]] = [i[0] for i in res]
        #print ",".join([i[0] for i in res])
        #print "\n-------"
    cnx.close()
    return retval

def getDBVersionNumbers(vlookup):
    cnx = getConnection("information_schema")
    cursor = cnx.cursor()
    query = ("select table_schema, table_name from tables where table_name like \"%wp_options%\";")
    cursor.execute(query)
    retval = {}
    #get database version numbers
    for item in cursor:
        #print(item[0])
        newCon = getConnection(item[0])
        c1 = newCon.cursor()
        query2 = ("select option_value from "+item[1]+" where option_name = \"db_version\" or option_name = \"siteurl\"")
        c1.execute(query2)
        res = c1.fetchall()
        #print res
        retval[item[0]] = vlookup[res[0][0]]
        #print ",".join([i[0] for i in res])
        #print "\n-------"
    cnx.close()
    return retval

def findPostsWith(keywords, versions, users):
    print "SEARCHING FOR KEYWORDs: ", keywords
    cnx = getConnection("information_schema")
    cursor = cnx.cursor()
    query = ("select table_schema, table_name from tables where table_name like \"%wp_posts%\";")
    cursor.execute(query)
    #get database version numbers
    for item in cursor:
        #print(item[0])
        newCon = getConnection(item[0])
        c1 = newCon.cursor()
        query2 = "select ID,post_content from "+item[1]+" where ";
        for i in keywords[:-1]:
            query2 += " post_content like \"%"+i+"%\" or ";
        query2 += " post_content like \"%"+keywords[-1]+"%\" ";
        query2 += ("and " if (len(keywords) > 0) else " ") + " post_type != \"revision\" and post_type != \"postman_sent_mail\"";
        #print query2
        c1.execute(query2)
        res = c1.fetchall()
        if(c1.rowcount > 0):
            print "site: ", item[0]
            print "version: ", versions[item[0]]
            print "number of hits ", c1.rowcount
            print "users : ", ",".join(users[item[0]])
            print "offending post ids: ",
            for i in res:
                print i[0],
            print "\n-------"
        for res in c1:
            pass
            #print res[0],
    cnx.close()

users = getDBusers()
versions = getDBVersionNumbers(versionLookup)

#findPostsWith(["cialis"], versions, users)
#findPostsWith(["viagra"], versions, users)
#findPostsWith(["cialis"], versions, users)
#findPostsWith(["tadalafil"], versions, users)
#findPostsWith(["hepatitis"], versions, users)
#findPostsWith(["sovaldion"], versions, users)
#findPostsWith(["sildenafil"], versions, users)
