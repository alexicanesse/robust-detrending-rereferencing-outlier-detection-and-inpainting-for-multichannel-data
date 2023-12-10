# EEG and MEG Data Preprocessing

This repository implements the robust detrending, rereferencing, outlier detection, and inpainting techniques proposed by Alain de Cheveigné and Dorothée Arzounian in their paper titled "Robust detrending, rereferencing, outlier detection, and inpainting for multichannel data" [1].

## Overview

Electroencephalography (EEG), magnetoencephalography (MEG), and related techniques often suffer from glitches, slow drifts, and other artifacts that can interfere with data analysis. The methods presented in this repository aim to address these issues through robust detrending, rereferencing, outlier detection, data interpolation (inpainting), step removal, and filter ringing artifact removal.

## Usage

To apply these techniques to your data, follow these steps:

1. **Read the Paper**: Familiarize yourself with the techniques described in the [research article](https://www.sciencedirect.com/science/article/pii/S1053811918300351).
2. **Clone the Repository**: Clone this repository to your local machine.

   ```bash
   git clone git@github.com:alexicanesse/robust-detrending-rereferencing-outlier-detection-and-inpainting-for-multichannel-data.git
   ```
3. **Install Dependencies** : Ensure you have the necessary dependencies installed. You can find them in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Code** : Utilize the provided Python notebook to launch the code and test it on your EEG or MEG data.

## Contributors

- Esteban Christiann (esteban.christiann@ens-paris-saclay.fr)
- Alexi Canesse (alexi.canesse@ens-lyon.fr)

## References

[1] Alain de Cheveigné, Dorothée Arzounian,
"Robust detrending, rereferencing, outlier detection, and inpainting for multichannel data",
*NeuroImage*,
Volume 172,
2018,
Pages 903-912,
ISSN 1053-8119,
[https://doi.org/10.1016/j.neuroimage.2018.01.035](https://doi.org/10.1016/j.neuroimage.2018.01.035).
[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1053811918300351)
