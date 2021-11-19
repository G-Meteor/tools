# coding=utf-8

import queue
import threading
import time

# ****线程数量

exitFlag = 0
THREAD_NUM = 10  # 线程数量
queueLock = threading.Lock()

# threadList = ["Thread-1", "Thread-2", "Thread-3"]

# 处理队列中数据
def consumer(workQueue):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = workQueue.get()
            # 功能句
            #print("Thread-%s processing %s" % (data, data))
            print(threading.currentThread())
        queueLock.release()
        time.sleep(0)


# 创建线程
def createThreads(target, args):
    threads = []
    for i in range(0, THREAD_NUM):
        threadID = i+1
        # thread = myThread(threadID, workQueue)
        thread = threading.Thread(target=target, args=args)
        # print(thread.getName())
        thread.start()
        threads.append(thread)
    return threads


# 填充队列
def fillQueue(workQueue):
    nameList = ["One", "Two", "Three", "Four", "Five"]
    for word in nameList:
        queueLock.acquire()
        workQueue.put(word)
        queueLock.release()
    return workQueue

# 等待所有任务处理完成
def waitTask2End(workQueue, threads):
    # 等待队列清空
    while not workQueue.empty():
        pass
    # 通知线程是时候退出
    global exitFlag
    exitFlag = 1
    # 等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")


if __name__ == "__main__":
    workQueue = queue.Queue()
    threads = createThreads(target=consumer, args=(workQueue,))
    #print("main:"+str(threading.activeCount()))
    workQueue2 = fillQueue(workQueue)
    print(threading.activeCount())
    #print(threading.enumerate())
    waitTask2End(workQueue2, threads)

# class myThread (threading.Thread):
#     def __init__(self, threadID, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.q = q
#
#     def run(self):
#         print("开启线程:Thread-" + str(self.threadID) + " ******")
#         process_data(self.threadID, self.q)
#         print("退出线程:Thread-" + str(self.threadID)+" ******")
