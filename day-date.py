date = "12/25/25T 10:28:40AM"

months_dist = {
     1:'January',
     2:'February',
     3:'March',
     4:'April',
     5:'May',
     6:'June',
     7:'July',
     8:'August',
     9:'September',
     10:'October',
     11:'Novermber',
     12:'December'
}


m = int(date.split("/")[0])
d = date.split("/")[1]
y = date.split("/")[2][:2]
# print(m, d, y)

res_date = f"{d} {months_dist[m]} 20{y}"
print(res_date)

hour = date.split("T")[1][:3].replace(" ", "")
minutes = date.split("T")[1][4:6]
seconds = date.split("T")[1][7:9]
# print(seconds)
am_pm = date.split("T")[1][-2:]
# print(hour, minutes)

res_time = f"{hour}:{minutes}:{seconds}{am_pm}"
print(res_time)