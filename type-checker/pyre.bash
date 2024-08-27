pdm add pyre-check

pdm run pyre init

pdm run pyre > pyre.errors

pdm run pyre --strict --source-directory src > pyre-strict.errors

pdm run pyre --source-directory typing > example-errors/pyre.errors
 
pdm run pyre --strict --source-directory typing > example-errors/pyre-strict.errors

