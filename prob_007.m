% By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
% see that the 6^(th) prime is 13.
% 
% What is the 10001^(st) prime number?

% Ans: 104743

clear
close all

plist = 2;

count = 10001;

tic

for i=2:count
  plist = growPrimeList(plist);
end

toc

disp(plist(end))
