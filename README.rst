=======
Audicus
=======


.. image:: https://readthedocs.org/projects/audicus/badge/?version=latest
        :target: https://audicus.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://codecov.io/github/amninder/audicus/graph/badge.svg?token=5iv9EmFSPs
         :target: https://codecov.io/github/amninder/audicus


Coverage
--------

.. image:: https://codecov.io/github/amninder/audicus/graphs/sunburst.svg?token=5iv9EmFSPs
         :alt: Code Coverage


Config
------

* The configuration can be overridden using **.env** file. The sample is provided in **.env.example** at the root level.
* following are the sample envs:

.. code-block:: bash

    FLASK_RUN_HOST="0.0.0.0"
    FLASK_RUN_PORT="6000"
    PYTHONPATH="."


How to run?
-----------

* In order to spin up the server, run the following command:

.. code-block:: bash

   docker-compose up


Api Details?
------------

* Following are the two api endpoints:

#. To get number of statuses: **localhost:6000/**

   * Response data type is:

     .. code-block:: json

         {
           "status_count": {
              "active": 1,
              "cancelled": 2,
              "on-hold": 3
           }
         }

#. To get average length of any given subscription: **localhost:6000/subscription/<sub_id>/orders/**

   * Response data tupe is:

     .. code-block:: json

         {
           "average_days": 23
         }
