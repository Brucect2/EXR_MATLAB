function [img, channels] = exrread(fn)

    f_path = mfilename('fullpath');
    f_path_full = strcat(f_path, '.m');
    filepath = fileparts(f_path_full);
    tmpMAT_path = strcat(filepath, '/tmp.mat');
    
    scripts = strcat('python', {' '}, filepath, '/process_exr.py ', {' '}, fn, {' '}, tmpMAT_path);
    
    system(scripts{1});
    load(tmpMAT_path)
    scripts = strcat('rm -r -f', {' '}, tmpMAT_path);
    system(scripts{1});
end

