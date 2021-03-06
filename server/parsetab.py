
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '1EEF96EEFEBEB6B124DDDAF8B5685870'
    
_lr_action_items = {'LBRACE':([0,2,3,4,5,6,7,9,11,12,13,14,16,17,18,21,22,23,24,25,29,30,],[2,2,-10,-11,-26,-9,-25,-12,2,-27,-10,-9,2,2,-28,-7,-8,-6,-14,-5,2,2,]),'MINUS':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[8,8,-10,-11,-26,-9,-25,-12,8,8,-27,-10,-9,8,8,8,-28,-7,-8,-6,-14,-5,-22,-23,-21,8,8,-19,-20,-18,-16,-17,-15,]),'EQUAL':([0,2,4,5,7,9,10,12,15,18,19,20,24,25,26,27,28,31,32,33,34,35,36,],[-13,-13,17,-26,-25,-24,19,-27,19,-28,29,30,-14,-5,-22,-23,-21,-19,-20,-18,-16,-17,-15,]),'STR':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[5,5,-10,-11,-26,-9,-25,-12,5,5,-27,-10,-9,5,5,5,-28,-7,-8,-6,-14,-5,-22,-23,-21,5,5,-19,-20,-18,-16,-17,-15,]),'$end':([0,1,3,4,5,6,7,9,10,11,12,18,21,22,23,24,25,26,27,28,31,32,33,34,35,36,],[-13,0,-2,-11,-26,-1,-25,-12,-4,-3,-27,-28,-7,-8,-6,-14,-5,-22,-23,-21,-19,-20,-18,-16,-17,-15,]),'RBRACE':([2,4,5,7,9,12,13,14,15,16,18,21,22,23,24,25,26,27,28,31,32,33,34,35,36,],[-13,-11,-26,-25,-12,-27,-10,-9,24,25,-28,-7,-8,-6,-14,-5,-22,-23,-21,-19,-20,-18,-16,-17,-15,]),'IDEN':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[7,7,-10,-11,-26,-9,-25,-12,7,7,-27,-10,-9,7,7,7,-28,-7,-8,-6,-14,-5,-22,-23,-21,7,7,-19,-20,-18,-16,-17,-15,]),'NUM':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[12,12,-10,-11,-26,-9,-25,18,-12,12,12,-27,-10,-9,12,12,12,-28,-7,-8,-6,-14,-5,-22,-23,-21,12,12,-19,-20,-18,-16,-17,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'dict':([0,2,11,16,17,29,30,],[3,13,21,21,26,31,34,]),'atom':([0,2,10,11,15,16,17,29,30,],[4,4,20,22,20,22,27,32,35,]),'dictcontents':([0,2,],[10,15,]),'list':([0,2,11,16,17,29,30,],[6,14,23,23,28,33,36,]),'empty':([0,2,],[9,9,]),'listcontents':([0,2,],[11,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> list','start',1,'p_start_list','paradoxparser.py',57),
  ('start -> dict','start',1,'p_start_dict','paradoxparser.py',61),
  ('start -> listcontents','start',1,'p_start_listc','paradoxparser.py',65),
  ('start -> dictcontents','start',1,'p_start_dictc','paradoxparser.py',69),
  ('list -> LBRACE listcontents RBRACE','list',3,'p_list','paradoxparser.py',73),
  ('listcontents -> listcontents list','listcontents',2,'p_listcontents_list','paradoxparser.py',77),
  ('listcontents -> listcontents dict','listcontents',2,'p_listcontents_dict','paradoxparser.py',81),
  ('listcontents -> listcontents atom','listcontents',2,'p_listcontents_atom','paradoxparser.py',85),
  ('listcontents -> list','listcontents',1,'p_listcontents_list_one','paradoxparser.py',89),
  ('listcontents -> dict','listcontents',1,'p_listcontents_dict_one','paradoxparser.py',93),
  ('listcontents -> atom','listcontents',1,'p_listcontents_atom_one','paradoxparser.py',101),
  ('listcontents -> empty','listcontents',1,'p_listcontents_empty','paradoxparser.py',105),
  ('empty -> <empty>','empty',0,'p_empty','paradoxparser.py',109),
  ('dict -> LBRACE dictcontents RBRACE','dict',3,'p_dict','paradoxparser.py',113),
  ('dictcontents -> dictcontents atom EQUAL list','dictcontents',4,'p_dictcontents','paradoxparser.py',117),
  ('dictcontents -> dictcontents atom EQUAL dict','dictcontents',4,'p_dictcontents','paradoxparser.py',118),
  ('dictcontents -> dictcontents atom EQUAL atom','dictcontents',4,'p_dictcontents','paradoxparser.py',119),
  ('dictcontents -> dictcontents EQUAL EQUAL list','dictcontents',4,'p_dictcontents_oddball','paradoxparser.py',123),
  ('dictcontents -> dictcontents EQUAL EQUAL dict','dictcontents',4,'p_dictcontents_oddball','paradoxparser.py',124),
  ('dictcontents -> dictcontents EQUAL EQUAL atom','dictcontents',4,'p_dictcontents_oddball','paradoxparser.py',125),
  ('dictcontents -> atom EQUAL list','dictcontents',3,'p_dictcontents_end','paradoxparser.py',129),
  ('dictcontents -> atom EQUAL dict','dictcontents',3,'p_dictcontents_end','paradoxparser.py',130),
  ('dictcontents -> atom EQUAL atom','dictcontents',3,'p_dictcontents_end','paradoxparser.py',131),
  ('dictcontents -> empty','dictcontents',1,'p_dictcontents_end2','paradoxparser.py',135),
  ('atom -> IDEN','atom',1,'p_atom','paradoxparser.py',139),
  ('atom -> STR','atom',1,'p_atom','paradoxparser.py',140),
  ('atom -> NUM','atom',1,'p_atom','paradoxparser.py',141),
  ('atom -> MINUS NUM','atom',2,'p_atom_neg','paradoxparser.py',145),
]
