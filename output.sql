CREATE TABLE Users (
UserID Int PRIMARY KEY,
Age Int
);

CREATE TABLE Books (
BookID Int PRIMARY KEY,
Title Varchar
);

CREATE TABLE LibraryLoans (
LoanID Int PRIMARY KEY,
Date Datetime,
CONSTRAINT fk_userid FOREIGN KEY (UserID) REFERENCES Users(UserID),
CONSTRAINT fk_bookid FOREIGN KEY (BookID) REFERENCES Books(BookID),
Returned Bool
);