import pymysql

# 连接到 MySQL 数据库
def get_connection():
    return pymysql.connect(
        host='localhost',    # 数据库主机
        user='root',         # 数据库用户名
        password='123456', # 数据库密码
        database='test_db',  # 数据库名称
        charset='utf8mb4'
    )
def insert_data():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
            cursor.execute(sql, ('Alice', 30))  # 插入数据
            connection.commit()  # 提交事务
            print("Data inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
def fetch_data():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetchall()  # 获取所有结果
            for row in result:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
def update_data():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE users SET age = %s WHERE name = %s"
            cursor.execute(sql, (35, 'Alice'))  # 更新数据
            connection.commit()  # 提交事务
            print("Data updated successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
def delete_data():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE name = %s"
            cursor.execute(sql, ('Alice',))  # 删除数据
            connection.commit()  # 提交事务
            print("Data deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
def create_table():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL
            )
            """
            cursor.execute(sql)
            connection.commit()
            print("Table created successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    create_table()  # 创建表
    insert_data()   # 插入数据
    fetch_data()    # 查询数据
    update_data()   # 更新数据
    delete_data()   # 删除数据
