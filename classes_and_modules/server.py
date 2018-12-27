class Server:

    def __init__(self, cpu, mem, disk, os):
        self.cpu = cpu
        self.mem = mem
        self.disk = disk
        self.__os = os

    def set_cpu(self, cpu):
        self.cpu = cpu

    def get_cpu(self):
        return self.cpu

    def set_mem(self, mem):
        self.mem = mem

    def get_mem(self):
        return self.mem

    def set_disk(self, disk):
        self.disk = disk

    def get_disk(self):
        return self.disk

    def set_os(self, os):
        self.__os = os

    def get_os(self):
        return self.__os

    def get_attribute(self):
        print(f'{self.cpu}核CPU，{self.mem}G内存，{self.disk}G磁盘空间，{self.__os}')


class ServerPrice(Server):

    def __init__(self, cpu, mem, disk, os, cpu_price, mem_price, disk_price):
        # Server.__init__(self, cpu, mem, disk, os, cpu_price, mem_price, disk_price)
        super(ServerPrice, self).__init__(cpu, mem, disk, os)
        self.cpu_price = cpu_price
        self.mem_price = mem_price
        self.disk_price = disk_price

    def set_cpu_price(self, cpu_price):
        self.cpu_price = cpu_price

    def get_cpu_price(self):
        return self.cpu_price

    def set_mem_price(self, mem_price):
        self.mem_price = mem_price

    def get_mem_price(self):
        return self.mem_price

    def set_disk_price(self, disk_price):
        self.disk_price = disk_price

    def get_disk_price(self):
        return self.disk_price

    def get_server_price(self):
        server_price = (self.cpu*self.cpu_price+self.mem*self.mem_price+self.disk*self.disk_price)
        print(f'服务器价格为{round(server_price, 2)}')


if __name__ == "__main__":
    # server = Server(8, 40, 150, "Linux")
    serverprice = ServerPrice(8, 40, 150, "Linux", 1527.679, 100.21, 50.789)
    # server.get_attribute()
    serverprice.get_attribute()
    serverprice.get_server_price()


