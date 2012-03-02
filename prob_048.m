function prob_048

% The series, 
% 
%     1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
% 
% Find the last ten digits of the series, 
%
%     1^1 + 2^2 + 3^3 + ... + 1000^1000.
%
%
% A: 9110846700
%

nDigits = 10;
base = 10^nDigits;

% Index of last summand
N = 1000;

val = 0;

for i = 1:N
  val = val + pow_a_b_mod_n(i, i, base);
  val = mod(val, base);
  
end

disp(sym(val))

return
