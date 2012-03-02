% Problem 43
%
% The number, 1406357289, is a 0 to 9 pandigital number because it is made
% up of each of the digits 0 to 9 in some order, but it also has a rather
% interesting sub-string divisibility property.
%
% Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
% note the following:
% 
%     * d2d3d4  = 406 is divisible by 2
%     * d3d4d5  = 063 is divisible by 3
%     * d4d5d6  = 635 is divisible by 5
%     * d5d6d7  = 357 is divisible by 7
%     * d6d7d8  = 572 is divisible by 11
%     * d7d8d9  = 728 is divisible by 13
%     * d8d9d10 = 289 is divisible by 17
% 
% Find the sum of all 0 to 9 pandigital numbers with this property.
% 
%
% Ans 16695334890
%

function prob_043

clear

listRight = 17 * (1:floor(1000/17));

divisors = [13 11 7 5 3 2 1];

for i = 1:numel(divisors)
  p = divisors(i);
  listLeft = p * (1:floor(1000/ p));

  listRight = processLists(listLeft, listRight, i);
  
  
end

sym(sum(listRight))


return

function listOut = processLists(listLeft, listRight, nTrailing)

powTen = 10^nTrailing;
listOut = zeros(numel(listLeft)*numel(listRight), 1);

count = 0;
for i = 1:numel(listRight)
  inds = mod(listLeft,100) == floor(listRight(i) / powTen);
  if any(inds)
    temp = listLeft(inds);
    temp = temp * powTen;
    temp = temp + mod(listRight(i), powTen);
    temp = temp(temp > 0);
    listOut(count+1: count + numel(temp)) = temp;
    count = count + numel(temp);
    
  end
 
end

listOut = listOut(1:count);
listOut = removeRowsWithRepeats(listOut);

return

function output = removeRowsWithRepeats(input)

temp = num2str(input);

[r,c] = size(temp);
temp = strrep(reshape(temp, 1,[]) , ' ', '0');
temp = reshape(temp, r, c);
inds = ones(r,1);

for i = 1:r
  if numel(unique(temp(i,:))) == c
    continue;
  end
  inds(i) = 0;
end
output = input(inds > 0, :);


return
