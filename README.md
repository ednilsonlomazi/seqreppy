## Description
Seqreppy is a Python library for numerical representations of genomic sequences.

## Installation

First, lets build the Seqreppy Core: SeqrepC.

For this, you will need to install distutils:

```
sudo apt install python3-distutils
```

Then you can follow the steps bellow:
1) Download the code and unzip the content
2) Go to SeqrepC-1.0.0/seqrepc folder
3) Run the command bellow:

```
sudo python3 setup.py install
```

Now, just install Seqreppy library as usual with pip:

```
pip install seqreppy
```


## Usage
I wrote bellow some code examplifying the functionalities of Seqreppy

```
from seqreppy.sp import sp # Core Functionalities

## -- -- -- -- -- -- -- -- Seqreppy Core Functionalities -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## Seqreppy uses SeqrepC module for do the following core operations
## SeqrepC is writed in C language

##-- sp.encode_from_file(<methods signatures>, <directory of fasta file>)
encodings = sp.encode_from_file(("cgr", "icgr"), "/home/ednilson/file.fasta")

##-- Using just one representation method
# encodings = sp.encode_from_file("cgr", "/home/ednilson/file.fasta")

##-- Using 2 or more sequences on memory.
# encodings = sp.encode_from_strings(("cgr", "icgr"), ("ATCCCGA", "CTGGGA")) 

##-- Using just 1 sequence on memory.
# encodings = sp.encode_from_strings(("cgr", "icgr"), "ATCCGAATCGA"))

##--! IMPORTANT NOTE 1 !--##
##-- Encodings are a dictionary. Each value of it is an iterable
##-- representing a pool of sequences encoded by the respectivelly
##-- method signature, corresponding to the keys of dictionary.
##-- If your file has 3 sequeces, encodings["cgr"][1] get the second
##-- sequece. If your file has just one sequence, it will be the first: 
##-- encodings["cgr"][0], following the order of appereance on fasta file.

##-- I have 2 encoding methods, so, 2 destinies
sp.save_results(encodings, "/dir/cgr.txt", "/dir/icgr.txt")

##-- In case just one encoding method, one destiny
# sp.save_results(encodings, "/home/ednilson/la")

# sp.get_results receives a dict, in with the keys are the method signatures
# and the values are the location (directory)
z = sp.get_results({"cgr": "/dir/cgr.txt", "icgr": "/dir/icgr.txt"})

##-- In case just one encoding method, one location
# z = sp.get_results({"atomic": "/home/ednilson/la"})

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

   
```
Currently, Seqreppy has 16 numerical representation methods identified by the signatures below:

* atomic
* cgr
* imaginary
* dna_walk
* liao
* eiip
* binary2b
* binary4b
* integer
* icgr
* molecular_mass
* paired_numeric
* real
* tetrahedron
* voss
* zcurve

if you wanna numerical representations details, you can read [a short summary here](nr_summary.pdf)

If you need some graphical visualisation, bellow is some methods you can use additionally to the core functionalities written above:

```
from seqreppy.sp import sp # Core Functionalities
from seqreppy.gsp import gsp # !-- Optional --! Genomic Signal Processing
from seqreppy.view import view # !-- Optional --! -> Graphical visualizations

## -- -- -- -- -- -- -- -- -- OPTIONAL MODULES  -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## just in case if you want to analyse graphically or
## apply some Genomic Signal Processing analysis

##-- lets get the results saved before
encodings = sp.get_results({"cgr": "/dir/cgr.txt", "icgr": "/dir/icgr.txt"})

##-- view.visualize(<method signature>, <sequence>)
view.visualize("cgr", encodings["cgr"][0])
view.visualize("icgr", encodings["icgr"][0])

##-- view.save_figure(<method signature>, <sequence>, <kargs>)
view.save_figure("cgr", encodings["cgr"][0], dpi=600, fname="file_name.png")

##-- kargs are not a rule. You can leave it with None.
view.save_figure("cgr", encodings["cgr"][0])

##-- lets get some encodings for apply gsp analysis
z = sp.encode_from_file("atomic", "/home/ednilson/file.fasta")

##-- gsp.apply_gsp(<function>, <encodings>)
z = gsp.apply_gsp(gsp.power_spectrum, z)

##-- view.visualize_power_spectrum(<method signature>, <sequence>, <kargs>) 
view.visualize_power_spectrum("atomic", z["atomic"][0])

##-- you can specify a range of the power spectrum
view.visualize_power_spectrum("atomic", z["atomic"][0], start=1, end=100)

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

```

## Contributing
If you have some new method developed by you or that is not present on Seqreppy,
please, contribute!
If you see some code that can be writed in a more efficient way, great! Let me know! 
If you saw interpretation erros in methods implementation, please, tell me, and i will make the corrections as soon as possible!

## Licence and Copyright
#### NumPy 
[Required NumPy copyrigh notes](https://github.com/numpy/numpy/blob/master/LICENSE.txt):

Copyright (c) 2005-2020, NumPy Developers.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
       copyright notice, this list of conditions and the following
       disclaimer in the documentation and/or other materials provided
       with the distribution.

    * Neither the name of the NumPy Developers nor the names of any
       contributors may be used to endorse or promote products derived
       from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#### Matplotlib
[License agreement for matplotlib versions 1.3.0 and later](https://github.com/matplotlib/matplotlib/blob/master/LICENSE/LICENSE)

1. This LICENSE AGREEMENT is between the Matplotlib Development Team
("MDT"), and the Individual or Organization ("Licensee") accessing and
otherwise using matplotlib software in source or binary form and its
associated documentation.

2. Subject to the terms and conditions of this License Agreement, MDT
hereby grants Licensee a nonexclusive, royalty-free, world-wide license
to reproduce, analyze, test, perform and/or display publicly, prepare
derivative works, distribute, and otherwise use matplotlib
alone or in any derivative version, provided, however, that MDT's
License Agreement and MDT's notice of copyright, i.e., "Copyright (c)
2012- Matplotlib Development Team; All Rights Reserved" are retained in
matplotlib  alone or in any derivative version prepared by
Licensee.

3. In the event Licensee prepares a derivative work that is based on or
incorporates matplotlib or any part thereof, and wants to
make the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to matplotlib .

4. MDT is making matplotlib available to Licensee on an "AS
IS" basis.  MDT MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, MDT MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. MDT SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any
relationship of agency, partnership, or joint venture between MDT and
Licensee.  This License Agreement does not grant permission to use MDT
trademarks or trade name in a trademark sense to endorse or promote
products or services of Licensee, or any third party.

8. By copying, installing or otherwise using matplotlib ,
Licensee agrees to be bound by the terms and conditions of this License
Agreement.

#### SeqrepC

BSD 3-Clause License

Copyright (c) 2020, Ednilson Lomazi
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#### Python

1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"), and
   the Individual or Organization ("Licensee") accessing and otherwise using Python
   3.9.1rc1 software in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, PSF hereby
   grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
   analyze, test, perform and/or display publicly, prepare derivative works,
   distribute, and otherwise use Python 3.9.1rc1 alone or in any derivative
   version, provided, however, that PSF's License Agreement and PSF's notice of
   copyright, i.e., "Copyright © 2001-2020 Python Software Foundation; All Rights
   Reserved" are retained in Python 3.9.1rc1 alone or in any derivative version
   prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on or
   incorporates Python 3.9.1rc1 or any part thereof, and wants to make the
   derivative work available to others as provided herein, then Licensee hereby
   agrees to include in any such work a brief summary of the changes made to Python
   3.9.1rc1.

4. PSF is making Python 3.9.1rc1 available to Licensee on an "AS IS" basis.
   PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY OF
   EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
   WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
   USE OF PYTHON 3.9.1rc1 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 3.9.1rc1
   FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
   MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 3.9.1rc1, OR ANY DERIVATIVE
   THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach of
   its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any relationship
   of agency, partnership, or joint venture between PSF and Licensee.  This License
   Agreement does not grant permission to use PSF trademarks or trade name in a
   trademark sense to endorse or promote products or services of Licensee, or any
   third party.

8. By copying, installing or otherwise using Python 3.9.1rc1, Licensee agrees
   to be bound by the terms and conditions of this License Agreement.
