import unittest
import pizza
import pizzahelp
import os
import shutil


class TestOrders(unittest.TestCase):

    def setUp(self):
        self.testOrder = pizza.Order()
        self.testOrder.orderList = {'svet': 10}

        self.statusOrder = pizza.Order()

        self.programPath = os.path.dirname(os.path.realpath(__file__))
        self.dirList = os.listdir(self.programPath)
        self.length = len(self.dirList)

    def tearDown(self):
        pizza.Order.instances = {}
        self.newDirList = os.listdir(self.programPath)
        for item in self.newDirList:
            if item not in self.dirList:
                os.remove(item)

    def test_if_name_in_order_list(self):
        self.testOrder.takeOrder('svet', 10)
        self.assertEqual(20, self.testOrder.orderList['svet'])

    def test_if_name_not_in_order_list(self):
        self.testOrder.takeOrder('rado', 20)
        self.assertEqual({'svet': 10, 'rado': 20}, self.testOrder.orderList)

    def test_order_status_if_nobody_ordered(self):
        result = self.statusOrder.getStat()
        self.assertEqual(pizzahelp.noOrdersYet, result)

    def test_order_status_if_someone_ordered(self):
        result = self.testOrder.getStat()
        self.assertEqual(self.testOrder.orderList, result)

    def test_save_order_if_nobody_ordered(self):
        result = len(self.dirList)
        self.assertEqual(self.statusOrder.saveOrder(), pizzahelp.noOrdersYet)
        self.assertEqual(result, self.length)

    def test_save_order_if_somebody_ordered(self):
        self.testOrder.saveOrder()
        self.assertEqual({}, self.testOrder.orderList)
        result = len(self.dirList)
        self.assertEqual(result, self.length)

    def test_list_orders_when_there_are_none(self):
        for filename in os.listdir("."):
            if filename.startswith("orders_"):
                os.rename(filename, "_%s" % filename)
        result = self.statusOrder.listOrders()
        self.assertEqual(result, pizzahelp.noOrderRecords)
        for filename in os.listdir("."):
            if filename.startswith("_orders_"):
                os.rename(filename, filename[1:])

    def test_load_order_when_there_are_existing_records(self):
        self.statusOrder.orderFiles = {1: "orders_2014_10_22_00_00_00"}
        self.filename1 = "orders_2014_10_22_00_00_00"
        self.contents1 = """'svet' - 10\n'rado' - 20"""
        with open(self.filename1, 'w+') as f:
            f.write(self.contents1)
        result = self.statusOrder.loadOrder()
        self.assertEqual(result, self.statusOrder.orderList)

    def test_load_order_when_no_order_exists(self):
        self.statusOrder.orderFiles = {}
        result = self.statusOrder.loadOrder()
        self.assertEqual("There are no order records.", result)

    def test_finish_program_with_non_existing_data(self):
        result = self.statusOrder.finish()
        self.assertEqual(pizzahelp.finishMessage, result)

    def test_finish_with_unsaved_data(self):
        result = self.testOrder.finish()
        if input == "finish":
            self.assertEqual(result, pizzahelp.finishMessage)
        if input == "save":
            self.assertEqual({}, self.testOrder.orderList)


if __name__ == "__main__":
    unittest.main()
