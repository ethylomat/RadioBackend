from django import forms

from .models import Channel, ChannelSet, ChannelFile, ChannelParameter


# Form for creating and editing channels

class ChannelForm(forms.ModelForm):
    class Meta:
             model = Channel
             fields = ('title', 'description', 'from_frequency', 'to_frequency', 'channel_set',)

    title = forms.CharField(required=True)
    channel_set = forms.ModelChoiceField(ChannelSet.objects.all(), required=True)
    from_frequency = forms.FloatField(required=True, label="Lower frequency")
    to_frequency = forms.FloatField(required=True, label="Higher frequency")

    def clean(self):
        super(ChannelForm, self).clean()
        from_frequency = self.cleaned_data.get('from_frequency')
        to_frequency = self.cleaned_data.get('to_frequency')

        try:
            if from_frequency < 0 or from_frequency > 1:
                self._errors['from_frequency'] = self.error_class([
                    'Lower frequency must be in between 0 and 1'])
            if to_frequency < 0 or to_frequency > 1:
                self._errors['to_frequency'] = self.error_class([
                    'Higher frequency must be in between 0 and 1'])
            if from_frequency > to_frequency:
                self._errors['from_frequency'] = self.error_class([
                    'Lower frequency must lower than higher frequency'])
                self._errors['to_frequency'] = self.error_class([
                    'Higher frequency must higher than lower frequency'])
        except:
            pass
        return self.cleaned_data




# Form for creating and editing channelsets

class ChannelSetForm(forms.ModelForm):
    title = forms.CharField(required=True)
    class Meta:
         model = ChannelSet
         fields = ('title',)


# Form for deleting channels

class DeleteChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = []


# Form for deleting channelsets

class DeleteChannelSetForm(forms.ModelForm):
    class Meta:
        model = ChannelSet
        fields = []
