import pymysql
from collections import OrderedDict


class OrderedDictCursor(pymysql.cursors.DictCursorMixin, pymysql.cursors.Cursor):
    dict_type = OrderedDict


class Database:
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            port=3307,
            user="root",
            password="123456",
            db="space",
            charset="utf8",
        )
        # self.cursor= self.db.cursor(pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor(OrderedDictCursor)

    # 회원관리
    # 로그인 확인
    def logcheck(self, cusid, password):
        sql = "select CustomerName from CUSTOMER WHERE Customer_ID = %s AND Password = %s;"
        print("로그인 시도")
        result = self.cursor.execute(sql, (cusid, password))
        name = self.cursor.fetchone()
        if result == 0:
            return False, ""
        else:
            return True, name  # 로그인 성공

    # 회원가입
    def registerCus(self, id, password, name, email):
        sql = "INSERT INTO `space`.`customer` (`Customer_ID`, `Password`, `CustomerName`, `Email`) VALUES (%s, %s, %s, %s)"
        result = self.cursor.execute(sql, (id, password, name, email))
        name = self.cursor.fetchone()
        if result == 0:
            return False
        else:
            return True, name  # 회원가입 성공

    # 회원탈퇴
    def withdrawlCus(self, id, password):
        sql = "select CustomerName from CUSTOMER WHERE Customer_ID=%s AND Password = %s"
        result = self.cursor.execute(sql, (id, password))
        name = self.cursor.fetchone()
        if result == 0:  # 인증실패
            return False
        else:  # 인증성공
            sql = "DELETE FROM `space`.`customer` WHERE `Customer_ID` = %s AND `Password` = %s"
            result = self.cursor.execute(sql, (id, password))
            name = self.cursor.fetchone()
            self.db.commit()
            print("회원탈퇴 성공")
            return True

    # CUSTOMER INFORMATION
    # 고객 개인정보 불러오기
    def getCusInfo(self, id):
        sql = "SELECT * FROM `space`.`customer` where `customer_id` = %s;"
        num = self.cursor.execute(sql, (id))
        data = self.cursor.fetchone()
        return data

    # 개인정보 변경
    def update_Customer(self, Password, Email, Customer_ID):
        sql = "UPDATE Customer SET Password = %s, Email = %s WHERE Customer_ID = %s;"
        result = self.cursor.execute(sql, (Password, Email, Customer_ID))
        self.db.commit()
        print("개인정보 변경 완료")

    # COUPON
    # 쿠폰 불러오기
    def getCoupon(self, id):
        sql = "select Coupon from CUS_COUPON where CUSTOMER_Customer_ID = %s;"
        num = self.cursor.execute(sql, (id))
        data = self.cursor.fetchall()
        return num, data

    # 쿠폰 사용 후 삭제
    def deleteCoupon(self, Coupon, Customer_ID):
        sql = "DELETE FROM `space`.`cus_coupon` WHERE (`Coupon` = %s) and (`CUSTOMER_Customer_ID` = %s);"
        result = self.cursor.execute(sql, (Coupon, Customer_ID))
        self.db.commit()
        print(Customer_ID + " : " + Coupon + "쿠폰 사용완료")

    # ADDRESS
    # 기존 배송지 정보 불러오기
    def getAddress(self, id):
        sql = "select Address from CUS_ADDRESS where CUSTOMER_Customer_ID = %s;"
        num = self.cursor.execute(sql, (id))
        data = self.cursor.fetchall()
        return num, data

    # 기존 배송지 변경
    def updateAddress(self, Address, Customer_ID, pastAddress):
        sql = "UPDATE cus_address SET Address = %s WHERE CUSTOMER_Customer_ID = %s AND Address = %s;"
        result = self.cursor.execute(sql, (Address, Customer_ID, pastAddress))
        self.db.commit()
        print(Customer_ID + " : " + Address + "주소 변경 완료")

    # 신규 배송지 추가
    def insertAddress(self, id, address):
        sql = "INSERT INTO `space`.`cus_address` (`Address`, `CUSTOMER_Customer_ID`) VALUES (%s, %s);"
        result = self.cursor.execute(sql, (address, id))
        self.db.commit()
        print(id + " : " + address + "주소 추가 완료")

    # 배송지 삭제
    def deleteAddress(self, Address, Customer_ID):
        sql = "DELETE FROM `space`.`cus_address` WHERE (`Address` = %s) and (`CUSTOMER_Customer_ID` = %s);"
        result = self.cursor.execute(sql, (Address, Customer_ID))
        self.db.commit()
        print(Customer_ID + " : " + Address + "주소 삭제 완료")

    def getinfluencer(self, infid):
        sql = "select * from influencer where AdminID = %s;"
        num = self.cursor.execute(sql, (infid))
        data = self.cursor.fetchone()
        return num, data

    # 재홍
    # 해당 고객의 거래내역(주문번호,일자,수량,idinventory) 띄우기
    def getCUS_TRANS(self, id):
        sql = "SELECT idTRANS, DateSold, SellPrice, Quantity, INVENTORY_idINVENTORY FROM TRANS JOIN TRANS_has_INVENTORY ON idTRANS = TRANS_idTRANS WHERE Cancellation = 'No' AND CUSTOMER_Customer_ID = %s ORDER BY idTRANS DESC;"
        num = self.cursor.execute(sql, (id))
        data = self.cursor.fetchall()
        return num, data

    # 그 거래내역 눌렀을 때 해당 transid가지는 주문내역 띄우기 -> 얘는 필요없음
    def getTRANS_h_I(self, transid):
        sql = "SELECT trans_idtrans, inventory_idinventory, sellprice, quantity FROM TRANS_has_INVENTORY WHERE TRANS_idTRANS = %s;"
        num = self.cursor.execute(sql, (transid))
        data = self.cursor.fetchall()
        return num, data

    # idinventory가지고 제품이름,사이즈, 색상 가져오기
    def getPRODUCT_INVENTORY(self, idINVENTORY):
        sql = "SELECT ProductName, Size, Color FROM PRODUCT JOIN INVENTORY ON ProductName = PRODUCT_ProductName WHERE idINVENTORY = %s;"
        num = self.cursor.execute(sql, (idINVENTORY))
        data = self.cursor.fetchall()
        return num, data

    # idtrans 해당하는 row cancellation update하기
    def Update_TRANS(self, idTRANS):
        sql = "UPDATE TRANS SET Cancellation = 'Yes' WHERE idTRANS = %s;"
        result = self.cursor.execute(sql, (idTRANS))
        self.db.commit()
        print(str(idTRANS) + " 환불 완료")

    # 상품 리뷰리뷰 작성~
    def Update_T_h_IReview(self, Review, idtrans, idinventory):
        sql = "UPDATE TRANS_has_INVENTORY SET Review = %s WHERE TRANS_idTRANS = %s AND INVENTORY_idINVENTORY = %s ;"
        result = self.cursor.execute(sql, (Review, idtrans, idinventory))
        self.db.commit()
        print(str(idtrans) + " : " + Review + "리뷰 작성")

    # 정렬 순 (상품)
    def showItemOrder(self, index, order):
        sql = (
            "SELECT Brand, ProductName, Price FROM PRODUCT ORDER BY "
            + index
            + " "
            + order
        )
        # sql = "SELECT Brand, ProductName, Price FROM PRODUCT ORDER BY %s %s"
        num = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    # 정렬 순 (스타일)
    def showStyleOrder(self, index, order):
        sql = (
            "SELECT StyleID ,ADMIN_AdminID, Description FROM STYLE ORDER BY "
            + index
            + " "
            + order
        )
        num = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    # 인벤 데이터 가져오기
    def getInventoryItem(self, pivot, productName):
        sql = (
            "SELECT distinct("
            + pivot
            + ") FROM inventory where product_productName = %s;"
        )
        num = self.cursor.execute(sql, (productName))
        data = self.cursor.fetchall()
        return num, data

    def getProductInfo(self, productName):
        sql = "SELECT * FROM product where productName = %s;"
        num = self.cursor.execute(sql, (productName))
        data = self.cursor.fetchone()
        return num, data

    # 카테고리 클릭했을 때 해당 상품명 띄워주기
    def getCategory(self, category):
        sql = (
            'SELECT Brand, ProductName, Price FROM PRODUCT WHERE Category = "'
            + category
            + '"'
        )
        num = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    # 상품명 눌렀을 때 리뷰 띄워주기
    def getReview(self, productName):
        sql = (
            'SELECT CUSTOMER_Customer_ID, Review FROM TRANS JOIN TRANS_has_INVENTORY ON TRANS_idTRANS = idTRANS WHERE REVIEW IS NOT NULL AND INVENTORY_idINVENTORY IN(SELECT idINVENTORY FROM INVENTORY WHERE PRODUCT_ProductName= "'
            + productName
            + '")'
        )
        num = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    # 해당 influencer 눌렀을 때 styleID 보여줌
    def getinfluencer_Style(self, id):
        sql = (
            'SELECT StyleID ,ADMIN_AdminID, Description FROM STYLE WHERE ADMIN_AdminID = "'
            + id
            + '"'
        )
        num = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    # 해당 상품명 눌렀을 때 StyleID 보여줌
    def PRODUCT_StyleID(self, productName):
        sql = (
            'SELECT StyleID ,ADMIN_AdminID, Description FROM STYLE WHERE StyleID IN (SELECT STYLE_StyleID FROM STYLE_has_PRODUCT WHERE PRODUCT_ProductName = "'
            + productName
            + '")'
        )
        num = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    # 해당 스타일 눌렀을 때 product 보여줌
    def Style_PRODUCT(self, styleid):
        sql = (
            "SELECT ProductName, Brand, Price FROM PRODUCT WHERE productName in (SELECT PRODUCT_productName FROM space.style_has_product WHERE STYLE_styleID = "
            + str(styleid)
            + " )"
        )
        num = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    # 해당 제품 눌렀을 때 그 제품의 누적 판매량을 보여줌
    def countCumSold(self, id):
        sql = (
            "SELECT SUM(Quantity) AS sum FROM TRANS_has_INVENTORY WHERE TRANS_idTRANS IN (SELECT idTRANS FROM TRANS WHERE Cancellation = 'No') AND INVENTORY_idINVENTORY IN (SELECT idINVENTORY FROM INVENTORY WHERE PRODUCT_ProductName = \""
            + id
            + '")'
        )
        num = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    # 구매시 trans추가
    def insertTrans(self, cusid, payment, totalPrice, dateSold, deliveryAddress):
        sql = "INSERT INTO TRANS (CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) VALUES(%s, %s, %s, %s, %s);"
        result = self.cursor.execute(
            sql, (cusid, payment, totalPrice, dateSold, deliveryAddress)
        )
        self.db.commit()
        print(
            cusid
            + " : "
            + payment
            + ","
            + str(totalPrice)
            + ","
            + dateSold
            + ","
            + deliveryAddress
            + " 구매완료"
        )

    def getTransID(self, cusid, payment, totalPrice, dateSold, deliveryAddress):
        sql = "SELECT idTRANS FROM TRANS WHERE CUSTOMER_Customer_ID = %s AND Payment = %s AND TotalPrice = %s AND DateSold = %s AND DeliveryAddress = %s;"
        num = self.cursor.execute(
            sql, (cusid, payment, totalPrice, dateSold, deliveryAddress)
        )
        data = self.cursor.fetchone()
        return num, data

    # 구매시 inventory추가
    def insertT_h_I(self, trans_id, inven_id, sellprice, quantity):
        sql = "INSERT INTO TRANS_has_INVENTORY (TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity) VALUES (%s, %s, %s, %s);"
        result = self.cursor.execute(sql, (trans_id, inven_id, sellprice, quantity))
        self.db.commit()

    def getInvenID(self, size, color, productName):
        sql = "SELECT idINVENTORY FROM INVENTORY WHERE size = %s AND color = %s AND PRODUCT_productName = %s;"
        num = self.cursor.execute(sql, (size, color, productName))
        data = self.cursor.fetchone()
        return num, data

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def commit():
        self.db.commit()
