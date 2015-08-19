myBlog
######

install
=======

pacchetti di supporto::

	$ easy_install -U Sphinx
	$ easy_install -U Tinkerer

blog
====

creiamo la struttura::

	$ mkdir myBlog && cd myBlog
	$ tinker --setup

configure
---------

modifichiamo il file di configurazione per le nostre impostazioni Es:
::

	# Change this to the name of your blog
	project = 'myBlog'

	# Change this to the tagline of your blog
	tagline = 'i miei appunti (by Orcim)'

	# Change this to your name
	author = 'orcim'

	# Change this to your copyright string
	copyright = '2015, ' + author

	# Change this to your blog root URL (required for RSS feed)
	website = 'http://127.0.0.1/blog/html/'

	# Localization
	language = "it"

per la sidebar::

	# Add templates to be rendered in sidebar here
	html_sidebars = {
	    '**': [ 'recent.html', 
	    		'searchbox.html', 
	    		'categories.html', 
	    		#'tags.html', 
	    		'tags_cloud.html',
	    		]
	}

post
----

Per tinkerer i posto sono informazioni temporali.

Iniziamo a postare (per compilare ci vuole almeno un post!)::

	$ tinker --post "This is the first post"

Editiamo il file che si troverà in **2015/08/18/This_is_the_first_post.rst**
e inseriamo il nostro post.

Se vogliamo creare l'effetto introduzione e il link **Continua a leggere..**
basterà suddividere il nostro posto in due parti suddivise dalla direttiva::

	.. more::

Se invece si volesse enfatizzare un blocco di codice si può usare le direttive relative::

	.. code-block:: rest
	.. code-block:: python

Se volessimo includer un file di codice::

.. literalinclude:: l00_start.py
    :language: python


page
----

Per tinkerer le pagine sono informazioni che non sono associate al tempo.

Creiamo la nostra prima pagina::

	$ tinker --page 'About'

compiler
--------

Per generare il codice statico::

	$ tinker -b



deployment
==========

Creare un **Blog** sfruttando la possibilità di pubblicarlo in rete attraverso il servizio **github**.

account
-------

Creare un account in **github** attraverso il pulsante new repository.
Creare un repository con il vostro nome. Nel mio caso: **orcim.github.io**

local
-----

Creiamo il nostro repository locale::

	echo "# orcim.github.io" >> README.md
	git init
	git add README.md
	git commit -m "first commit"

remote
------

Inizializziamo la futura gestione remota del nostro repository in modalità https::

	$ git remote add origin https://github.com/orcim/orcim.github.io.git

O inizializziamo la futura gestione remota del nostro repository in modalità ssh::

	$ git remote add origin git@github.com:orcim/orcim.github.io.git

visualizza il modo::

	$ git remote -v

modifichiamo in ssh::

	$ git remote set-url origin git@github.com:USERNAME/OTHERREPOSITORY.git
	$ git remote set-url origin git@github.com:orcim/orcim.github.io.git

modifichiamo in https::

	$ git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git
	$ git remote set-url origin https://github.com/orcim/orcim.github.io.git

Per vedere la configurazione::

	$ git config -l

Per autenticare in automatico in ssh::

- https://help.github.com/articles/generating-ssh-keys/
- https://help.github.com/articles/changing-a-remote-s-url/

Dopo aver creato il nostro blog possiamo creare il file **.gitignore**
per indicare cosa non si vuol gestire nel nostro repository.

Ricordiamo di creare un file vuoto **.nojekyll** che serve ad indicare che non useremo quella applicazione per gestire il nostro blog.

deploy
------

Infine possiamo pubblicare il nostro **Blog**::

	$ git push -u origin master

se non si è impostato l'autenticazione auto::

	user: orciml@gmail.com
	pass: 135790Azz 

view
----

per visualizzare il nostro blog attraverso il nostro browser preferito andiamo all'indirizzo:

- orcim.github.io



