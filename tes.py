import Process

for i in range(9):
    df = Process.proses(i)
    df.to_csv()