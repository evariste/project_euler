% A common security method used for online banking is to ask the user
% for three random characters from a passcode. For example, if the
% passcode was 531278, they may ask for the 2nd, 3rd, and 5th
% characters; the expected reply would be: 317.

% The text file, keylog.txt, contains fifty successful login attempts.

% Given that the three characters are always asked for in order,
% analyse the file so as to determine the shortest possible secret
% passcode of unknown length.

% Method, draw a graph and follow the nodes visually . . . 

% See prob_079.pdf

clear 
close all

fid = fopen('prob_079.txt', 'r');

data = fscanf(fid, '%u');
fclose(fid);


adjMat = zeros(10,10);

for i = 1:numel(data)
  val = data(i);

  nextDigit = mod(val, 10);
  val = floor(val / 10);

  while val > 0
    digit = mod(val, 10);
    adjMat(1+digit, 1+nextDigit) = 1;
    val = floor(val / 10);
    nextDigit = digit;
  end
  
  
end

nodeIds = num2str( (0:9)' );

inds = sum(adjMat + adjMat') > 0;
nodeIds = nodeIds(inds);
adjMat = adjMat(inds, inds);


bg = biograph(adjMat, nodeIds);

view(bg)

