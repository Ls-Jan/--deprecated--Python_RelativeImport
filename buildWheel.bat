

py setup.py sdist bdist_wheel

echo Y | rmdir build /s
echo Y | rmdir RelativeImport.egg-info /s

pause
