-- Database tables for CEG 701 Database principles project. 
-- Author: Shumin Guo. 

CREATE DATABASE IF NOT EXISTS CS701DB; 

USE CS701DB;

CREATE TABLE IF NOT EXISTS BankAccount (
   AcntId INT NOT NULL AUTO_INCREMENT,
   AcntName VARCHAR(20) NOT NULL, 
   AcntBlnc DOUBLE DEFAULT 0, 
   AcntDate DATE NOT NULL, 
   Memo TEXT, 
   PRIMARY KEY (AcntId)
)ENGINE=INNODB; 

CREATE TABLE IF NOT EXISTS Income (
   IcmId INT NOT NULL AUTO_INCREMENT, 
   IcmDate DATE NOT NULL,
   IcmAmunt DOUBLE DEFAULT 0,
   Memo TEXT, 
   PRIMARY KEY (IcmId)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS Spend (
   SpdId INT NOT NULL AUTO_INCREMENT,
   SpdDate DATE NOT NULL, 
   SpdLoc VARCHAR(100) NOT NULL, 
   SpdAmunt INT DEFAULT 0,
   Memo TEXT, 
   PRIMARY KEY (SpdId)
)ENGINE=INNODB; 

CREATE TABLE IF NOT EXISTS Deposit (
   DpId INT NOT NULL AUTO_INCREMENT,
   DpToAcnt INT NOT NULL, 
   DpFrom INT NOT NULL, 
   DpAmunt DOUBLE DEFAULT 0,
   DpDate DATE, 
   Memo TEXT,
   PRIMARY KEY (DpId),
   FOREIGN KEY (DpToAcnt) REFERENCES BankAccount(AcntId)
   	ON DELETE CASCADE ON UPDATE CASCADE, 
   FOREIGN KEY (DpFrom) REFERENCES Income(IcmId)
	ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=INNODB; 

CREATE TABLE IF NOT EXISTS Withdrawal (
   WdId INT NOT NULL AUTO_INCREMENT, 
   WdFrom INT NOT NULL, 
   WdFor INT NOT NULL, 
   WdAmunt DOUBLE DEFAULT 0,
   WdDate DATE NULL NULL, 
   Memo TEXT, 
   PRIMARY KEY (WdId), 
   FOREIGN KEY (WdFrom) REFERENCES BankAccount(AcntId)
   	ON DELETE CASCADE ON UPDATE CASCADE, 
   FOREIGN KEY (WdFor) REFERENCES Spend(SpdId)
	ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=INNODB; 
