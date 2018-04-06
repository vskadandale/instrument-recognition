# Musical Instrument Recognition in Solo-Instrument Recordings

### MIR Course, April 2018

#### Final project for MIR course by Venkatesh Shenoy Kadandale, 2017-18 SMC Master Student 


### Objective

To classify sounds from Good-Sounds dataset based on the musical instrument category. 


### Methodology

Two approaches are presented. In the first approach, the models are trained and tested on the actual sounds from the dataset. Low overall accuracy is expected. In the second approach, the models are trained and tested over the sounds after they are stripped off all the sinusoidal components i.e the residual components of the sounds. The overall accuracy is expected to improve in the second approach. The silent frames are dropped and low-level statistical features are extracted using Essentia's MusicExtractor. Among these, the top five features in terms of the variance in distribution will be shortlisted. Support Vector Machines(SVM) are used for classification.  


### Dataset

Subset of Good-Sounds Dataset. Here's the [link](https://www.upf.edu/web/mtg/good-sounds?sid=395) to the complete dataset. The original dataset is provided with a [CC BY-NC 4.0 license](). I have used only a subset of this dataset for this task. The original dataset has the following folder structure: 
```
.
  |-sax_alto_scale_raul_recordings
  |  |-neumann
  |  |-iphone
  |-saxo_tenor_raul_recordings
  |  |-neumann
  |-trumpet_ramon_timbre_stability
  |  |-neumann
  |  |-akg
  |-saxo_soprane_raul_recordings
  |  |-neumann
  |  |-iphone
  |-flute_almudena_evaluation_recordings
  |  |-iphone
  |-clarinet_pablo_attack
  |  |-neumann
  |  |-akg
  |-clarinet_pablo_timbre_stability
  |  |-neumann
  |  |-akg
  |-cello_nico_improvement_recordings
  |  |-neumann
  |  |-iphone
  |-piccolo_irene_recordings
  |  |-neumann
  |  |-iphone
  |-trumpet_jesus_improvement_recordings
  |  |-neumann
  |  |-iphone
  |-trumpet_ramon_attack_stability
  |  |-neumann
  |  |-akg
  |-violin_raquel_attack
  |  |-neumann
  |  |-akg
  |-saxo_raul_recordings
  |  |-neumann
  |  |-iphone
  |-clarinet_gener_evaluation_recordings
  |  |-iphone
  |-bass_alejandro_recordings
  |  |-neumann
  |-violin_laia_improvement_recordings
  |  |-neumann
  |-cello_margarita_open_strings
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-flute_almudena_reference
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-violin_violin_scales_laia_recordings
  |  |-neumann
  |-flute_almudena_attack
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-oboe_marta_recordings
  |  |-neumann
  |  |-iphone
  |-clarinet_pablo_dynamics_stability
  |  |-neumann
  |  |-akg
  |-flute_almudena_air
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-trumpet_ramon_reference
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-clarinet_marti_evaluation_recordings
  |  |-iphone
  |-trumpet_ramon_dynamics_stability
  |  |-neumann
  |  |-akg
  |-flute_almudena_reference_piano
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-trumpet_jesus_evaluation_recordings
  |  |-iphone
  |-cello_margarita_attack
  |  |-neumann
  |  |-akg
  |-sax_alto_scale_2_raul_recordings
  |  |-neumann
  |  |-iphone
  |-cello_margarita_reference
  |  |-neumann
  |  |-akg
  |-flute_josep_evaluation_recordings
  |  |-iphone
  |-violin_raquel_richness
  |  |-neumann
  |  |-akg
  |-flute_scale_irene_recordings
  |  |-neumann
  |  |-iphone
  |-sax_tenor_tenor_scales_2_raul_recordings
  |  |-neumann
  |-flute_almudena_stability
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-clarinet_pablo_air
  |  |-neumann
  |  |-akg
  |-clarinet_gener_improvement_recordings
  |  |-neumann
  |  |-iphone
  |-violin_raquel_reference
  |  |-neumann
  |  |-akg
  |-clarinet_scale_gener_recordings
  |  |-neumann
  |  |-iphone
  |-saxo_bariton_raul_recordings
  |  |-neumann
  |  |-iphone
  |-cello_margarita_dynamics_stability
  |  |-neumann
  |  |-akg
  |-cello_margarita_timbre_stability
  |  |-neumann
  |  |-akg
  |-flute_josep_improvement_recordings
  |  |-neumann
  |  |-iphone
  |-trumpet_ramon_evaluation_recordings
  |  |-iphone
  |-cello_margarita_timbre_richness
  |  |-neumann
  |  |-akg
  |-violin_raquel_timbre_stability
  |  |-neumann
  |  |-akg
  |-trumpet_ramon_air
  |  |-neumann
  |  |-akg
  |-sax_tenor_tenor_scales_raul_recordings
  |  |-neumann
  |-clarinet_pablo_richness
  |  |-neumann
  |  |-akg
  |-violin_raquel_dynamics_stability
  |  |-neumann
  |  |-akg
  |-flute_almudena_dynamics_change
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-clarinet_pablo_pitch_stability
  |  |-neumann
  |  |-akg
  |-trumpet_scale_jesus_recordings
  |  |-neumann
  |  |-iphone
  |-flute_almudena_timbre
  |  |-neumann
  |  |-akg
  |  |-iphone
  |-trumpet_ramon_pitch_stability
  |  |-neumann
  |  |-akg
  |-saxo_tenor_iphone_raul_recordings
  |  |-iphone
  |-violin_raquel_pitch_stability
  |  |-neumann
  |  |-akg
  |-cello_margarita_pitch_stability
  |  |-neumann
  |  |-akg
  |-clarinet_pablo_reference
  |  |-neumann
  |  |-akg
  |-violin_laia_improvement_recordings_2
  |  |-iphone

```


All the audio clips are segregated into folders based on the instrument categories: bass, cello, clarinet, flute, oboe, piccolo, saxophone, trumpet and violin. The following is the resulting folder structure: 
```
. 
  |-sax(3360 samples)
  |-pic(776 samples)
  |-flu(2308 samples)
  |-vio(1853 samples)
  |-cel(2118 samples)
  |-obo(494 samples)
  |-cla(3359 samples)
  |-bas(159 samples)
  |-tru(1883 samples)
```
As we see, dataset is severely unbalanced. To have a uniform distribution of data among all the instrument categories, I have randomly chosen 159 samples from each of the categories. This pruned and restructured version of the original dataset is considered for this project. The sounds from this subset are further split into their sinusoidal and residual components. The Essentia music extractor has been used to extract the lowlevel statistical features for all these three categories: original sound, residual and sinusoidal. All these processed/pre-extracted data are temporarily made available [here](https://drive.google.com/open?id=1yXBrGMo8Kh0k-UrAf1utOM_KlKyHkDiZ).


## NOTE:

The dataset, by itself, is not best suited for instrument classification task as the sound categories being considered, do not represent the diversity of musical instruments. There are no percussion instruments. The sound samples are categorized not just based on instruments but also by the way they are played. These sub-categorizations give an in-depth representation of the instrument. It makes sense to treat sub-categories as different instruments since their textures are drastically different in some cases. For example, a violin pluck sounds totally different from a bowed sound. Also, some sounds involve noise generated by the musician. For example, breathing sounds while playing flute. Again, these sounds are not there in all the flute samples, they have critical presence in some sub-categories. Due to all these factors, we need to decide which instrument sub-categories are to be merged and which ones need to be considered seperate. This involves careful inspection of sounds from all the 61 sub-categories. This is beyond the scope of this project. In this project, we will be merging all the sounds based on instruments without taking into account the sub-category(which tells us how it was played). Also, sax-alto, sax-tenor, sax-soprano and sax-baritone are merged. One more drawback is that the dataset is unbalanced, which forces us to remove samples from the dataset so that each class has same number of samples. Also, for this project, the sounds are randomly selected. Hence, the distribution of sounds with respect to sub-categories of sounds are not uniform. The project does not aim to arrive at the feature set or the classifier parameters that gives the best classification accuracy. The objective here is to study the effect of dataset refinement(separating out the residual/sinusoidal) on classification accuracy keeping the feature set and classifier parameters fixed.



## References

Romani Picas O. Dabiri D., Serra X. "A real-time system for meauring sound goodness in instrumental sounds" 138th Audio Engineering Society Convention, Warsarw, 2015
