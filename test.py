#!/usr/bin/python
import speedtest
import mysql.connector
import time

print("    ____      __                       __     __  ____                     ")
print("   /  _/___  / /____  _________  ___  / /_   /  |/  (_)_____________  _____")
print("   / // __ \/ __/ _ \/ ___/ __ \/ _ \/ __/  / /|_/ / / ___/ ___/ __ \/ ___/")
print(" _/ // / / / /_/  __/ /  / / / /  __/ /_   / /  / / / /  / /  / /_/ / /    ")
print("/___/_/ /_/\__/\___/_/  /_/ /_/\___/\__/  /_/  /_/_/_/  /_/   \____/_/")

while(True):
        test = speedtest.Speedtest()
        test.get_servers()
        best = test.get_best_server()
        download_result = test.download()
        upload_result = test.upload()
        ping_result = test.results.ping
        print(f"Download speed: {download_result / 1024 / 1024:.2f}Mbit/s")
        print(f"Upload speed: {upload_result / 1024 / 1024:.2f}Mbit/s")
        print(f"Ping: {ping_result}ms")

        mydb = mysql.connector.connect(
          host="localhost",
          user="app",
          password="Computer1!",
          database="Connections"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO speedtest (speedup, speeddown, ping, server) VALUES (%s, %s, %s, %s)"
        val = (int(download_result / 1024 / 1024), int(upload_result / 1024 / 1024), int(ping_result), "Server: " + str(best['host']) + " located in " + str(best['country']))
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        time.sleep(300)
