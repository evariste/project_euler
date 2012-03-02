N = 3;
facN = factorial(N);

id = 1:N;

elts = 1:facN;
invElts = zeros(1:facN, 1);


maxEdges = facN * (facN-1) / 2;
fromList = zeros(maxEdges, 1);
toList = zeros(maxEdges, 1);
edgeCount = 0;
idList = cell(facN, 1);

for i = 0:facN-1

  p1 = factoradic2perm(index2factoradic(i, N));
  idList{i+1} = num2str(p1);
%   pInv = inversePermutation(p1);
%   factInv = perm2factoradic(pInv);
%   iInv = factoradic2index( factInv );
%   disp([num2str(i+1) ' = ' num2str(p1) ' | ' num2str(iInv+1) ' = ' num2str(pInv)])
%   invElts(i + 1) = iInv + 1;
  
  
  indCurr = i;
  pCurr = p1;
  indNext = -1;
  pNext = [];
  
  while any(pCurr ~= id)
    pNext = p1(pCurr);
    factNext = perm2factoradic(pNext);
    indNext  = factoradic2index(factNext);
    
    edgeCount = edgeCount + 1;
    fromList(edgeCount) = indCurr + 1;
    toList(edgeCount) = indNext + 1;
    
    pCurr = pNext;
    indCurr = indNext;
   
  end
  
end

% adjMat = sparse(elts, invElts, ones(size(elts)), facN, facN);
fromList = fromList(1:edgeCount);
toList = toList(1:edgeCount);
adjMat = sparse(fromList, toList, ones(size(fromList)), facN, facN);


view(biograph(adjMat, idList))

