## Description
Seqreppy is a Python library for numerical representations of genomic sequences.

## Instalation
First, you need to install NumPy 1.16.2 and Matplotlib 3.0.2, which are Seqreppy dependencies.
After that, just clone this repository.

## Usage
First of all, make sure that your main Python program is in the same directory (folder) as Seqreppy, after the clone step performed previously.
I wrote below a simple code that resumed the Seqreppy core functionalities:

```
from seqreppy.encoder.repseq import RepSeq # main class with management purpose
repseq = RepSeq() # instantiate RepSeq
repseq.set_fasta_file("/directory/of/fasta/file.fasta") # tell where is the file containing the sequences to be encoded
repseq.set_models("DnaWalk", "CGR") # tell the methods you want to use specifying your signatures 
results = repseq.perform_encoding() # encode
print(results["CGR"]) # results is a dictionary, where the keys are the methods signatures.   
```
Currently, Seqreppy has 16 numerical representation methods identified by the signatures below:

* Atomic
* CGR
* Complex
* DnaWalk
* Yau
* Eiip
* Binary2B
* Binary4B
* Integer
* IntegerCGR
* MolecularMass
* PairedNumericMapping
* Real
* Tetrahedron
* Voss
* Zcurve

if you wanna numerical representations details, you can read [a short summary here](numerical_representations_summary.pdf)

If you need some graphical visualisation, bellow is some methods you can use additionally to the core functionalities written above:

```
repseq.generate_figure(0, "DnaWalk") # 0 is the sequence id (appearance in the fasta file) and the next argument is the representation method
repseq.generate_figure(0, "DnaWalk", save=True) # If you don't wanna see and just save the figure (default saving directory is seqreppy/results/img)
repseq.generate_figure(0, "DnaWalk", save=True, fname="file-name.png", dpi=600) # You can specify image properties too
```

In cases where you need to save the results to the disk and collect it in the future, execute:

```
repseq.save_results("/directory/of/dnawalk/results") # default saving directory is seqreppy/results/txt/method_signature
repseq.get_results({"DnaWalk": "/directory/of/dnawalk/results"})
```

## Contributing
If you have some new method developed by you or that is not present on DnaNR,
please, contribute!
If you see some code that can be writed in a more efficient way, great! Let me know! Remeber, the code is focous on velocity. Because of that, some parts may be a little hard to read.
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
