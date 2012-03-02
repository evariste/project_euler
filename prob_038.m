% Take the number 192 and multiply it by each of 1, 2, and 3:
% 
%     192 × 1 = 192 192 × 2 = 384 192 × 3 = 576
% 
% By concatenating each product we get the 1 to 9 pandigital, 192384576. We
% will call 192384576 the concatenated product of 192 and (1,2,3)
% 
% The same can be achieved by starting with 9 and multiplying by 1, 2, 3,
% 4, and 5, giving the pandigital, 918273645, which is the concatenated
% product of 9 and (1,2,3,4,5).
% 
% What is the largest 1 to 9 pandigital 9-digit number that can be formed
% as the concatenated product of an integer with (1,2, ... , n) where n >
% 1?
% 
% A: 932718654

function prob_038

% possible values for n in k * [1,2,... , n]
ns  = [2    3   4   5 6 9];

% possible values for k such that the sum of the numbers of digits of the
% results  equals 9 (only way to be pan-digital)
kLo = [5000 100 25  5 3 1];
kHi = [9999 333 33 10 3 1];

maxVal = 0;

for i = 1:numel(ns);
  seq = 1:ns(i);
  for k = kLo(i):kHi(i);
    
    str = strrep(num2str(k * seq), ' ', '');
    val = str2double(str);
    str2 = unique(str);
    if findstr(str2, '0')
      continue
    end
    if length(str2) == 9 &&  maxVal < val
      maxVal = val;
      disp([k ns(i) val])
    end
      
  end
end

return
