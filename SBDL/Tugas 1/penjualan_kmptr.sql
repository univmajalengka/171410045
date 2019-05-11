-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2019 at 04:37 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `penjualan_kmptr`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_brg`
--

CREATE TABLE `data_brg` (
  `kdbrg` int(7) NOT NULL,
  `nmbrg` varchar(35) NOT NULL,
  `hrgbrg` decimal(8,0) NOT NULL,
  `satuan` int(10) NOT NULL,
  `stok` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data_brg`
--

INSERT INTO `data_brg` (`kdbrg`, `nmbrg`, `hrgbrg`, `satuan`, `stok`) VALUES
(111, 'Hardisk', '900000', 1, 100),
(112, 'Keyboard', '120000', 1, 50),
(113, 'Mouse', '60000', 1, 50),
(114, 'Motherboard', '2500000', 1, 25),
(115, 'Flashdisk', '135000', 1, 35),
(116, 'Ram', '300000', 1, 15),
(117, 'LCD', '550000', 1, 20),
(118, 'Prosesor', '650000', 1, 8),
(119, 'Battery Laptop', '700000', 1, 35),
(120, 'Charger Laptop', '400000', 1, 30);

-- --------------------------------------------------------

--
-- Table structure for table `data_plnggan`
--

CREATE TABLE `data_plnggan` (
  `noplg` int(7) NOT NULL,
  `nmplg` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `notlp` varchar(12) NOT NULL,
  `kota` varchar(25) NOT NULL,
  `tglgabung` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data_plnggan`
--

INSERT INTO `data_plnggan` (`noplg`, `nmplg`, `alamat`, `notlp`, `kota`, `tglgabung`) VALUES
(5001, 'Rifki', 'Sumedang', '089660754321', 'Sumedang', '2019-03-01'),
(5002, 'Crisda', 'Ligung', '089765123321', 'Majalengka', '2019-03-02'),
(5003, 'Dadan', 'Leuwimunding', '089543223100', 'Majalengka', '2019-03-03'),
(5004, 'Taufik', 'Tomo', '082334213900', 'Sumedang', '2019-03-04'),
(5005, 'Didin', 'Jatiwangi', '081120900176', 'Majalengka', '2019-03-05'),
(5006, 'Ahmad', 'Kadipaten', '087654321100', 'Majalengka', '2019-03-06'),
(5007, 'Dudung', 'Rajagaluh', '081990342139', 'Majalengka', '2019-03-07'),
(5008, 'Iqbal', 'Palasah', '085890123879', 'Majalengka', '2019-03-08'),
(5009, 'Herni', 'Maja', '087650543876', 'Majalengka', '2019-03-09'),
(5010, 'Isma', 'Talaga', '089765435900', 'Majalengka', '2019-03-10');

-- --------------------------------------------------------

--
-- Table structure for table `data_servis`
--

CREATE TABLE `data_servis` (
  `nofak` int(7) NOT NULL,
  `tglfak` date NOT NULL,
  `noplg` int(7) NOT NULL,
  `masalah` varchar(30) NOT NULL,
  `bayar` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data_servis`
--

INSERT INTO `data_servis` (`nofak`, `tglfak`, `noplg`, `masalah`, `bayar`) VALUES
(510, '2019-03-01', 5006, 'Kerusakan Flashdisk Ganti Baru', 150000),
(511, '2019-03-02', 5002, 'Kerusakan Hardisk', 100000),
(512, '2019-03-03', 5003, 'Ganti Keyboard', 200000),
(513, '2019-03-04', 5005, 'Ganti LCD', 600000),
(514, '2019-03-05', 5007, 'Ganti Mouse', 70000),
(515, '2019-03-06', 5009, 'Upgrade RAM', 400000),
(516, '2019-03-08', 5008, 'Ganti Battery Laptop', 800000),
(517, '2019-03-12', 5010, 'Kerusakan Prosesor', 750000),
(518, '2019-03-20', 5001, 'Ganti Motherboard', 2500000),
(519, '2019-03-21', 5004, 'Kerusakan Charger', 400000);

-- --------------------------------------------------------

--
-- Table structure for table `detail_faktur`
--

CREATE TABLE `detail_faktur` (
  `nofak` int(7) NOT NULL,
  `kdbrg` int(7) NOT NULL,
  `qty` int(4) NOT NULL,
  `bayar` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `detail_faktur`
--

INSERT INTO `detail_faktur` (`nofak`, `kdbrg`, `qty`, `bayar`) VALUES
(516, 119, 1, 700000),
(512, 112, 2, 250000),
(513, 117, 1, 550000),
(518, 114, 1, 2500000),
(514, 113, 1, 60000),
(519, 120, 1, 400000),
(510, 115, 1, 135000),
(511, 111, 1, 900000),
(517, 118, 1, 650000),
(515, 116, 1, 300000);

-- --------------------------------------------------------

--
-- Table structure for table `faktur`
--

CREATE TABLE `faktur` (
  `nofak` int(7) NOT NULL,
  `tglfak` date NOT NULL,
  `noplg` int(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `faktur`
--

INSERT INTO `faktur` (`nofak`, `tglfak`, `noplg`) VALUES
(516, '2019-03-01', 5006),
(511, '2019-03-02', 5002),
(512, '2019-03-03', 5003),
(513, '2019-03-04', 5005),
(518, '2019-03-20', 5001),
(514, '2019-03-05', 5007),
(515, '2019-03-06', 5009),
(517, '2019-03-12', 5010),
(519, '2019-03-21', 5004);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE `tbl_login` (
  `username` varchar(35) NOT NULL,
  `password` varchar(35) NOT NULL,
  `konfirmasi` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`username`, `password`, `konfirmasi`) VALUES
('admin', '48e76f37c4987f887a509574884b1fd4785', ''),
('admin1', '9f4e503be46f5646d25d5cbb8b31655caad', ''),
('admin3', 'cd0655e21233b5260c98eae6c5524e1f2c5', ''),
('admin4', '339ac0da0258789134e56ba5698f4ff12c4', ''),
('admin5', '5ae9ce42c8cc53312364aacc4ed44e17794', ''),
('admin6', '6b95e64245b9dcab887a45a111e9556ff7e', ''),
('admin7', '9cc62ce431a6f7f36e0e1df0099125c1eb0', ''),
('admin8', 'bd4b26eaaa2de45707eaa9ac863ba172a97', ''),
('admin9', '2ab071d31a5b0b78b20404061d17ae00f25', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_brg`
--
ALTER TABLE `data_brg`
  ADD PRIMARY KEY (`kdbrg`);

--
-- Indexes for table `data_plnggan`
--
ALTER TABLE `data_plnggan`
  ADD PRIMARY KEY (`noplg`);

--
-- Indexes for table `data_servis`
--
ALTER TABLE `data_servis`
  ADD PRIMARY KEY (`nofak`),
  ADD KEY `noplg` (`noplg`);

--
-- Indexes for table `detail_faktur`
--
ALTER TABLE `detail_faktur`
  ADD KEY `nofak` (`nofak`),
  ADD KEY `kdbrg` (`kdbrg`);

--
-- Indexes for table `faktur`
--
ALTER TABLE `faktur`
  ADD KEY `noplg` (`noplg`),
  ADD KEY `nofak` (`nofak`);

--
-- Indexes for table `tbl_login`
--
ALTER TABLE `tbl_login`
  ADD PRIMARY KEY (`username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `data_servis`
--
ALTER TABLE `data_servis`
  ADD CONSTRAINT `data_servis_ibfk_1` FOREIGN KEY (`noplg`) REFERENCES `data_plnggan` (`noplg`);

--
-- Constraints for table `detail_faktur`
--
ALTER TABLE `detail_faktur`
  ADD CONSTRAINT `detail_faktur_ibfk_1` FOREIGN KEY (`kdbrg`) REFERENCES `data_brg` (`kdbrg`),
  ADD CONSTRAINT `detail_faktur_ibfk_2` FOREIGN KEY (`nofak`) REFERENCES `data_servis` (`nofak`);

--
-- Constraints for table `faktur`
--
ALTER TABLE `faktur`
  ADD CONSTRAINT `faktur_ibfk_1` FOREIGN KEY (`noplg`) REFERENCES `data_plnggan` (`noplg`),
  ADD CONSTRAINT `faktur_ibfk_2` FOREIGN KEY (`nofak`) REFERENCES `data_servis` (`nofak`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
