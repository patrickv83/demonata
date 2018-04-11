import java.util.List;

public class SampleDriver {
	public static void main(String args[]) {
		SampleDriver sampleDriver = new SampleDriver();
		//Player zoey = new Player("Zoey", 500, new Weapon("Pink Ribbon of Destruction", 3, 5, DamageType.SLASHING));
		//zoey.addResistance(DamageType.CHOPPING);
		Player donald = new Player("Hapless Adventurer", 45, new Weapon("Newbie cudgel", 2, 3, DamageType.BLUNT));
		
		Enemy goblin = new Enemy("Goblin", 30, new Weapon("Rusty Nailfile", 1, 4, DamageType.CHOPPING));
		goblin.addVulnerability(DamageType.SLASHING);
		List<Enemy> enemies = goblin.copy(goblin, 5);
		
		//sampleDriver.fight(zoey, enemies);
		sampleDriver.fight(donald, enemies);
		
	}
	
	public void fight(Player player, List<Enemy> enemies) {
		boolean allEnemiesDead = false;
		boolean playerAttacked = true;

		System.out.println(player.getName()+" engages "+enemies.size()+" vile enemies!");
		while(!player.isDead() && !allEnemiesDead) {
			playerAttacked = false;
			allEnemiesDead = true;
			for(int i=0; i<enemies.size(); i++) {
				Enemy enemy = enemies.get(i);
				if(!enemy.isDead()) {
					allEnemiesDead = false;
					if(!playerAttacked) {
						int playerDamage = player.attack(enemy);
						playerAttacked = true;
						System.out.println(player.getName()+" attacks "+enemy.getName()+" (Enemy "+i+") for "+playerDamage+" damage.");
					}
					int enemyDamage = enemy.attack(player);
					System.out.println(enemy.getName()+" attacks "+player.getName()+" for "+enemyDamage+" damage.");
					if(enemy.isDead()) {
						System.out.println(player.getName()+" has slain "+enemy.getName()+" (Enemy "+i+")!");
					}
					if(player.isDead()) {
						System.out.println(player.getName()+" has died, game over!");
						return;
					}
				}
			}
		}
		System.out.println(player.getName()+" has defeated all "+enemies.size()+" enemies while wielding a "+player.getWeapon().getName()+" and has "+player.getHitPoints()+" health remaining");
	}
}
