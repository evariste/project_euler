% Find the greatest product of five consecutive digits in the 1000-digit
% number. 

fid = fopen('prob_008.data');
str = textscan(fid, '%s');
fclose(fid);

str = char(str{1});

products = zeros(numel(str)-4, 1);

for i = 1:numel(str)-4
  products(i) = prod( str2num( regexprep(str(i:i+4), '(.)', '$1 ') ) );
end

[val, i] = max(products);

disp(['Product :' num2str(val)])

disp(['Sequence: ' str(i:i+4)])


