from rest_framework import serializers
from .models import incidents





class incidentSerializers(serializers.ModelSerializer):
    class Meta:
        model=incidents
        fields =['id','incident_id','reporter_name','incident_details','reported_date_time','priority','incident_status']

      
    def validate_incident_status(self, value):
        if self.instance and self.instance.incident_status == 'closed':
            raise serializers.ValidationError('Cannot update a closed incident')
        return value




