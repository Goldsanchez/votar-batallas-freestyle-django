from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
    
class Competition(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
    
class Season(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-name"]
    
class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
    
class Freestyler(models.Model):
    aka = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.aka
    
    class Meta:
        ordering = ["aka"]
    
class Battle(models.Model):
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    freestyler_1 = models.ForeignKey(Freestyler, related_name='freestyler_1', on_delete=models.CASCADE)
    freestyler_2 = models.ForeignKey(Freestyler, related_name='freestyler_2', on_delete=models.CASCADE)
    score_freestyler_1 = models.IntegerField(default=0)
    score_freestyler_2 = models.IntegerField(default=0)
    winner_replica = models.ForeignKey(Freestyler, related_name='winner_replica', default=13, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    incremental1MC1 = models.IntegerField(default=0)
    incremental2MC1 = models.IntegerField(default=0)
    incremental3MC1 = models.IntegerField(default=0)
    incremental4MC1 = models.IntegerField(default=0)
    incremental5MC1 = models.IntegerField(default=0)
    incremental6MC1 = models.IntegerField(default=0)
    incrementalTecnicaMC1 = models.IntegerField(default=0)
    incrementalFlowMC1 = models.IntegerField(default=0)
    incrementalEscenaMC1 = models.IntegerField(default=0)
    incrementalTotalMC1 = models.IntegerField(default=0)

    incremental1MC2 = models.IntegerField(default=0)
    incremental2MC2 = models.IntegerField(default=0)
    incremental3MC2 = models.IntegerField(default=0)
    incremental4MC2 = models.IntegerField(default=0)
    incremental5MC2 = models.IntegerField(default=0)
    incremental6MC2 = models.IntegerField(default=0)
    incrementalTecnicaMC2 = models.IntegerField(default=0)
    incrementalFlowMC2 = models.IntegerField(default=0)
    incrementalEscenaMC2 = models.IntegerField(default=0)
    incrementalTotalMC2 = models.IntegerField(default=0)

    random1MC1 = models.IntegerField(default=0)
    random2MC1 = models.IntegerField(default=0)
    random3MC1 = models.IntegerField(default=0)
    random4MC1 = models.IntegerField(default=0)
    random5MC1 = models.IntegerField(default=0)
    random6MC1 = models.IntegerField(default=0)
    randomTecnicaMC1 = models.IntegerField(default=0)
    randomFlowMC1 = models.IntegerField(default=0)
    randomEscenaMC1 = models.IntegerField(default=0)
    randomTotalMC1 = models.IntegerField(default=0)

    random1MC2 = models.IntegerField(default=0)
    random2MC2 = models.IntegerField(default=0)
    random3MC2 = models.IntegerField(default=0)
    random4MC2 = models.IntegerField(default=0)
    random5MC2 = models.IntegerField(default=0)
    random6MC2 = models.IntegerField(default=0)
    randomTecnicaMC2 = models.IntegerField(default=0)
    randomFlowMC2 = models.IntegerField(default=0)
    randomEscenaMC2 = models.IntegerField(default=0)
    randomTotalMC2 = models.IntegerField(default=0)

    minuto1IdaMC1 = models.IntegerField(default=0)
    minuto2IdaMC1 = models.IntegerField(default=0)
    minuto3IdaMC1 = models.IntegerField(default=0)
    minuto4IdaMC1 = models.IntegerField(default=0)
    minuto5IdaMC1 = models.IntegerField(default=0)
    minuto6IdaMC1 = models.IntegerField(default=0)
    minutoTecnicaIdaMC1 = models.IntegerField(default=0)
    minutoFlowIdaMC1 = models.IntegerField(default=0)
    minutoEscenaIdaMC1 = models.IntegerField(default=0)
    minutoTotalIdaMC1 = models.IntegerField(default=0)

    minuto1IdaMC2 = models.IntegerField(default=0)
    minuto2IdaMC2 = models.IntegerField(default=0)
    minuto3IdaMC2 = models.IntegerField(default=0)
    minuto4IdaMC2 = models.IntegerField(default=0)
    minuto5IdaMC2 = models.IntegerField(default=0)
    minuto6IdaMC2 = models.IntegerField(default=0)
    minutoTecnicaIdaMC2 = models.IntegerField(default=0)
    minutoFlowIdaMC2 = models.IntegerField(default=0)
    minutoEscenaIdaMC2 = models.IntegerField(default=0)
    minutoRespuesta1MC2 = models.IntegerField(default=0)
    minutoRespuesta2MC2 = models.IntegerField(default=0)
    minutoRespuesta3MC2 = models.IntegerField(default=0)
    minutoRespuesta4MC2 = models.IntegerField(default=0)
    minutoRespuesta5MC2 = models.IntegerField(default=0)
    minutoRespuesta6MC2 = models.IntegerField(default=0)
    minutoTotalIdaMC2 = models.IntegerField(default=0)

    minuto1VueltaMC1 = models.IntegerField(default=0)
    minuto2VueltaMC1 = models.IntegerField(default=0)
    minuto3VueltaMC1 = models.IntegerField(default=0)
    minuto4VueltaMC1 = models.IntegerField(default=0)
    minuto5VueltaMC1 = models.IntegerField(default=0)
    minuto6VueltaMC1 = models.IntegerField(default=0)
    minutoTecnicaVueltaMC1 = models.IntegerField(default=0)
    minutoFlowVueltaMC1 = models.IntegerField(default=0)
    minutoEscenaVueltaMC1 = models.IntegerField(default=0)
    minutoRespuesta1MC1 = models.IntegerField(default=0)
    minutoRespuesta2MC1 = models.IntegerField(default=0)
    minutoRespuesta3MC1 = models.IntegerField(default=0)
    minutoRespuesta4MC1 = models.IntegerField(default=0)
    minutoRespuesta5MC1 = models.IntegerField(default=0)
    minutoRespuesta6MC1 = models.IntegerField(default=0)
    minutoTotalVueltaMC1 = models.IntegerField(default=0)

    minuto1VueltaMC2 = models.IntegerField(default=0)
    minuto2VueltaMC2 = models.IntegerField(default=0)
    minuto3VueltaMC2 = models.IntegerField(default=0)
    minuto4VueltaMC2 = models.IntegerField(default=0)
    minuto5VueltaMC2 = models.IntegerField(default=0)
    minuto6VueltaMC2 = models.IntegerField(default=0)
    minutoTecnicaVueltaMC2 = models.IntegerField(default=0)
    minutoFlowVueltaMC2 = models.IntegerField(default=0)
    minutoEscenaVueltaMC2 = models.IntegerField(default=0)
    minutoTotalVueltaMC2 = models.IntegerField(default=0)

    deluxeEntrada1MC1 = models.IntegerField(default=0)
    deluxeEntrada2MC1 = models.IntegerField(default=0)
    deluxeEntrada3MC1 = models.IntegerField(default=0)
    deluxe1MC1 = models.IntegerField(default=0)
    deluxe2MC1 = models.IntegerField(default=0)
    deluxe3MC1 = models.IntegerField(default=0)
    deluxe4MC1 = models.IntegerField(default=0)
    deluxe5MC1 = models.IntegerField(default=0)
    deluxe6MC1 = models.IntegerField(default=0)
    deluxeTecnicaMC1 = models.IntegerField(default=0)
    deluxeFlowMC1 = models.IntegerField(default=0)
    deluxeEscenaMC1 = models.IntegerField(default=0)
    deluxeTotalMC1 = models.IntegerField(default=0)

    deluxeEntrada1MC2 = models.IntegerField(default=0)
    deluxeEntrada2MC2 = models.IntegerField(default=0)
    deluxeEntrada3MC2 = models.IntegerField(default=0)
    deluxe1MC2 = models.IntegerField(default=0)
    deluxe2MC2 = models.IntegerField(default=0)
    deluxe3MC2 = models.IntegerField(default=0)
    deluxe4MC2 = models.IntegerField(default=0)
    deluxe5MC2 = models.IntegerField(default=0)
    deluxe6MC2 = models.IntegerField(default=0)
    deluxeTecnicaMC2 = models.IntegerField(default=0)
    deluxeFlowMC2 = models.IntegerField(default=0)
    deluxeEscenaMC2 = models.IntegerField(default=0)
    deluxeTotalMC2 = models.IntegerField(default=0)

    replica1MC1 = models.IntegerField(default=0)
    replica2MC1 = models.IntegerField(default=0)
    replica3MC1 = models.IntegerField(default=0)
    replica4MC1 = models.IntegerField(default=0)
    replica5MC1 = models.IntegerField(default=0)
    replica6MC1 = models.IntegerField(default=0)
    replicaTecnicaMC1 = models.IntegerField(default=0)
    replicaFlowMC1 = models.IntegerField(default=0)
    replicaEscenaMC1 = models.IntegerField(default=0)
    replicaTotalMC1 = models.IntegerField(default=0)

    replica1MC2 = models.IntegerField(default=0)
    replica2MC2 = models.IntegerField(default=0)
    replica3MC2 = models.IntegerField(default=0)
    replica4MC2 = models.IntegerField(default=0)
    replica5MC2 = models.IntegerField(default=0)
    replica6MC2 = models.IntegerField(default=0)
    replicaTecnicaMC2 = models.IntegerField(default=0)
    replicaFlowMC2 = models.IntegerField(default=0)
    replicaEscenaMC2 = models.IntegerField(default=0)
    replicaTotalMC2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.freestyler_1} vs {self.freestyler_2}"
    
    class Meta:
        ordering = ["-id"]