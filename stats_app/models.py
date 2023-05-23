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
    score_freestyler_1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    score_freestyler_2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    winner_replica = models.ForeignKey(Freestyler, related_name='winner_replica', default=13, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    incremental1MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental2MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental3MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental4MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental5MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental6MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incrementalTecnicaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incrementalFlowMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incrementalEscenaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incrementalTotalMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    incremental1MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental2MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental3MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental4MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental5MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incremental6MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incrementalTecnicaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incrementalFlowMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incrementalEscenaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    incrementalTotalMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    random1MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random2MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random3MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random4MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random5MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random6MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    randomTecnicaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    randomFlowMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    randomEscenaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    randomTotalMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    random1MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random2MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random3MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random4MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random5MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    random6MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    randomTecnicaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    randomFlowMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    randomEscenaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    randomTotalMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    minuto1IdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto2IdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto3IdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto4IdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto5IdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto6IdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoTecnicaIdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoFlowIdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoEscenaIdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoTotalIdaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    minuto1IdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto2IdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto3IdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto4IdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto5IdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto6IdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoTecnicaIdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoFlowIdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoEscenaIdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta1MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta2MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta3MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta4MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta5MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta6MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoTotalIdaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    minuto1VueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto2VueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto3VueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto4VueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto5VueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto6VueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoTecnicaVueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoFlowVueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoEscenaVueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta1MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta2MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta3MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta4MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta5MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoRespuesta6MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoTotalVueltaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    minuto1VueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto2VueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto3VueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto4VueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto5VueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minuto6VueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoTecnicaVueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoFlowVueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoEscenaVueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    minutoTotalVueltaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    deluxeEntrada1MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeEntrada2MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeEntrada3MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe1MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe2MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe3MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe4MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe5MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe6MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeTecnicaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeFlowMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeEscenaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeTotalMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    deluxeEntrada1MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeEntrada2MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeEntrada3MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe1MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe2MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe3MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe4MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe5MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxe6MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeTecnicaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeFlowMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeEscenaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deluxeTotalMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    replica1MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica2MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica3MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica4MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica5MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica6MC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replicaTecnicaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replicaFlowMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replicaEscenaMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replicaTotalMC1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    replica1MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica2MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica3MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica4MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica5MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replica6MC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replicaTecnicaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replicaFlowMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replicaEscenaMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    replicaTotalMC2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.freestyler_1} vs {self.freestyler_2}"
    
    class Meta:
        ordering = ["-id"]