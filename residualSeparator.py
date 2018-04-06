import os
import sprModel as SPR
import wavio
from scipy.signal import get_window
import scipy
import stft as STFT

def main(path_to_original_dataset='/homedtic/vshenoykadandale/datasets/good-sounds/instruments'):
    
    """
    path_to_original_dataset: path to the original dataset whose residuals need to be separated.    
    """
    print("Checkpoint 1")
    path_to_residual_dataset=os.path.join(os.path.dirname(path_to_original_dataset),'residuals')
    if not os.path.exists(path_to_residual_dataset):
        os.umask(0) #To mask the permission restrictions on new files/directories being created
        os.makedirs(path_to_residual_dataset,0o755) # 0o777 gives us full permissions for the folder

    print("Checkpoint 2")
    instruments=sorted(os.listdir(path_to_original_dataset))
    for instrument in instruments:
        instrument_path=os.path.join(path_to_original_dataset,instrument)
        instrument_residual_path=os.path.join(path_to_residual_dataset,instrument)
        print("Checkpoint 3")
        if not os.path.exists(instrument_residual_path):
            os.umask(0) #To mask the permission restrictions on new files/directories being created
            os.makedirs(instrument_residual_path,0o755) # 0o777 gives us full permissions for the folder
        files=os.listdir(instrument_path)
        print("Processing [INSTRUMENT] "+instrument + " folder which contains " +str(len(files))+" files")
        for filename in files:
            file_path=os.path.join(instrument_path,filename)
            file_residual_path=os.path.join(instrument_residual_path,filename[:-4] + '_residual.wav')
             
            wav = wavio.read(file_path)
            x=wav.data
            fs=wav.rate
            sampwidth=wav.sampwidth
            w=get_window("hamming",2001)
            N=2048
            H=128
            minSineDur=0.02
            maxnSines=150
            freqDevOffset=10
            freqDevSlope=0.001
            t=-80
            Ns=512

            # perform sinusoidal plus residual analysis
            tfreq, tmag, tphase, xr = SPR.sprModelAnal(x, fs, w, N, H, t, minSineDur, maxnSines, freqDevOffset, freqDevSlope)

            # compute spectrogram of residual
            #mXr, pXr = STFT.stftAnal(xr, w, N, H)

            # sum sinusoids and residual
            #y, ys = SPR.sprModelSynth(tfreq, tmag, tphase, xr, Ns, H, fs)
            
            #wavio.write(outputFileSines, ys, fs, sampwidth)
            wavio.write(file_residual_path, xr, fs, sampwidth=sampwidth)
            #wavio.write(outputFile, y, fs, sampwidth)
    print("Successfully extracted residuals from all the audio files!")
if __name__ == "__main__":
        main()
