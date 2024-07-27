from rest_framework import serializers


class LocalTimeSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    timezone = serializers.CharField()
    local_time = serializers.DateTimeField()
    local_time_str = serializers.CharField()

    def validate(self, data):
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
            raise serializers.ValidationError("Invalid latitude or longitude values.")
        if data.get('timezone') is None:
            raise serializers.ValidationError("Timezone could not be determined.")
        if data.get('local_time') is None:
            raise serializers.ValidationError("Local time could not be determined.")
        if not data.get('local_time_str'):
            raise serializers.ValidationError("Local time string could not be determined.")
        return data


class ResultSerializer(serializers.Serializer):
    result = serializers.JSONField
