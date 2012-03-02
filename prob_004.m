% A palindromic number reads the same both ways. The largest palindrome
% made from the product of two 2-digit numbers is 9009 = 91 × 99.
% 
% Find the largest palindrome made from the product of two 3-digit numbers.

% Ans:       906609 = 913  * 993

for a = 9:-1:0
  for b = 9:-1:0
    for c = 9:-1:0
      pal = a * 100001 + b * 010010 + c * 001100;
      facs = factors(pal);

      % ignore factors that don't have 3 digits
      facs = facs(facs > 99 & facs < 1000);
      
      for i = 1:numel(facs)
        if (pal/facs(i)  > 99) && (pal/facs(i) < 1000)
          disp ([pal facs(i) pal/facs(i)])
          return
        end
      end

    end
  end
end
