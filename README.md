# AlexSofttek




SQL INSERT FOR TEST API

## Base de datos: `customer_order_status`

```bash
 
INSERT INTO `api_orderclass` (`id`, `order_number`, `item_name`, `status`) VALUES
(1, 'ORD_1567', 'LAPTOP', 'SHIPPED'),
(2, 'ORD_1567', 'MOUSE', 'SHIPPED'),
(3, 'ORD_1567', 'KEYBOARD', 'PENDING'),
(4, 'ORD_1234', 'GAME', 'SHIPPED'),
(5, 'ORD_1234', 'BOOK', 'CANCELLED'),
(6, 'ORD_1234', 'BOOK', 'CANCELLED'),
(7, 'ORD_9834', 'SHIRT', 'SHIPPED'),
(8, 'ORD_9834', 'PANTS', 'CANCELLED'),
(9, 'ORD_7654', 'TV', 'CANCELLED'),
(10, 'ORD_7654', 'DVD', 'CANCELLED');

```


## Base de datos: `detecting_change`

```bash
 

INSERT INTO `api_weatherclass` (`id`, `date`, `was_rainy`) VALUES
(1, '1/1/20', 'FALSE'),
(2, '1/2/20', 'TRUE'),
(3, '1/3/20', 'TRUE'),
(4, '1/4/20', 'FALSE'),
(5, '1/5/20', 'FALSE'),
(6, '1/6/20', 'TRUE'),
(7, '1/7/20', 'FALSE'),
(8, '1/8/20', 'TRUE'),
(9, '1/9/20', 'TRUE'),
(10, '1/10/20', 'TRUE');

```


## Base de datos: `season_problem`

```bash
 
INSERT INTO `api_seasonclass` (`id`, `ORD_ID`, `ORD_DT`) VALUES
(1, '113-8909896-6940269', '2019-09-23'),
(2, '114-0291773-7262677', '2020-01-01'),
(3, '114-0291773-7262697', '2019-12-05'),
(4, '114-9900513-7761000', '2020-09-24'),
(5, '112-5230502-8173028', '2020-01-30'),
(6, '112-7714081-3300254', '2020-05-02'),
(7, '114-5384551-1465853', '2020-04-02'),
(8, '114-7232801-4607440', '2020-10-09');

```
