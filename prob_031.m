% In England the currency is made up of pound, £, and pence, p, and there
% are eight coins in general circulation:
% 
%     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
% 
% It is possible to make £2 in the following way:
% 
%     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
% 
% How many different ways can £2 be made using any number of coins?
% 
% A: 73682
%
% Possible better approach using partial fractions of a generating function
% is available at:
%
% http://stackoverflow.com/questions/4243831/how-to-count-possible-combination-for-coin-problem
% 
function prob_031


coins = [200 100 50 20 10 5 2 1];
val = 200;

n = getCombs(val, coins);

return


function cs = getCombs(amount, coinSet)

if (amount == 0)
  cs = 1;
  return
end

if (amount < 0 || isempty(coinSet))
  cs = 0;
  return
end

withFirst = getCombs(amount - coinSet(1), coinSet);
withoutFirst = getCombs(amount, coinSet(2:end));
cs = withFirst + withoutFirst;

return