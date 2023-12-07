from bisect import insort

class Hand:
  labels = {
    'A': 14, 
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
  }

  def __init__(self, hand, bid):
    self.hand_ = hand
    self.bid_ = int(bid)
    self.type_ = self.get_type()
    self.order_ = self.get_ordering()

  def get_type(self):
    max_same_label = 0
    pair_found = False
    two_pair = False
    full_house = False
    found_cards = []
    for i in range(0, len(self.hand_)):
      if self.hand_[i] in found_cards:
        continue
      same_label = 0
      for j in range(i+1, len(self.hand_)):
        if self.hand_[i] == self.hand_[j]:
          same_label += 1
          if self.hand_[i] not in found_cards:
            found_cards.append(self.hand_[i])
      if same_label > max_same_label:
        max_same_label = same_label

      if pair_found and same_label == 1:
        two_pair = True
      if same_label == 1:
        pair_found = True

    if max_same_label == 4:
      return 'Five of a Kind'
    elif max_same_label == 3:
      return 'Four of a Kind'
    elif max_same_label == 2:
      if pair_found:
        return 'Full House'
      else:
        return 'Three of a Kind'
    elif max_same_label == 1:
      if two_pair:
        return 'Two Pair'
      else:
        return 'One Pair'
    elif max_same_label == 0:
      return 'High Card'
    
  def get_ordering(self):
    types = {
      'High Card': 0,
      'One Pair': 1,
      'Two Pair': 2,
      'Three of a Kind': 3,
      'Full House': 4,
      'Four of a Kind': 5,
      'Five of a Kind': 6
    }

    order = 0
    for i in range(0, len(self.hand_)):
      if self.hand_[i] in self.labels:
        order += self.labels[self.hand_[i]] * pow(100, len(self.hand_) - i - 1)
      else:
        order += int(self.hand_[i]) * pow(100, len(self.hand_) - i - 1)
    
    order += types[self.type_] * pow(100, len(self.hand_))
    return order
  
  def __lt__(self, other):
    return self.order_ < other.order_

  def __gt__(self, other):
    return self.order_ > other.order_

  def __eq__(self, other):
    return self.order_ == other.order_
  
  def __str__(self):
    return self.hand_ + ' ' + str(self.order_) + ' ' + self.type_
  
  def __repr__(self):
    return self.hand_ + ' ' + str(self.order_) + ' ' + self.type_
  


f = open('input.txt', 'r')

hands = []
for line in f:
  insort(hands, Hand(line[:5], line[6:-1]))

sum = 0
for i in range(len(hands)):
  sum += (i+1) * hands[i].bid_

print(sum)