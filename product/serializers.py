from rest_framework.serializers import ModelSerializer

from product.models import Event


class EventSerializer(ModelSerializer):
        def create(self, validated_data):
            event = Event(**validated_data)
            event.save()

        def update(self, instance, validated_data):
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
            return instance

        class Meta:
            model = Event
            fields = ["title", "thumbnail", "description", "dt_created", "exposure_start_date", "exposure_end_date"]
