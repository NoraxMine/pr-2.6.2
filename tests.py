# import threading
# import time

# def reading (file_name, data):
#     with open(file_name, 'w') as f:
#         f.write(data)
#         time.sleep(1)


# start = time.time()
# for i in range(1000):
#     reading(f"qwerty{i}", "joi")
# delta = time.time() - start
# print(delta)

# start1 = time.time()
# tr = []
# for i in range(1000):
#     t = threading.Thread(target=reading, args=(f"qwertyy{i}", "qwertyui"))
#     t.start()
#     tr.append(t)
# for t in tr:
#     t.join()
# delta1 = time.time() - start1
# print(delta1)




